import re
from core.audio_engine import say
from brains.llm_brain import askJarvis
from core.registry import TOOL_REGISTRY
from config.userPref import userName, callMe, location, preferredBrowser
from memory.memory_chroma import save_memory
import datetime
import subprocess


def greetings(muted=False):
    currentTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(currentTime[:2])

    if hour < 12:
        greeting_text = f"Good morning {userName} {callMe}! How can I help you today?"
    elif hour < 18:
        greeting_text = f"Good afternoon {userName} {callMe}! How can I help you today?"
    else:
        greeting_text = f"Good evening {userName} {callMe}! How can I help you today?"

    if not muted:
        say(greeting_text)
    else:
        print(greeting_text)


def performAction(task, muted=False):
    if not task:
        return
        
    answer = askJarvis(task)
    
    if answer:
        action_match = re.search(r"\[ACTION:\s*(.*?)\s*\]", answer, re.DOTALL)
        
        if action_match:
            spoken_text = answer.replace(action_match.group(0), "").strip()
        else:
            spoken_text = answer.strip()
            
        if spoken_text:
            save_memory(task, spoken_text, str(datetime.datetime.now().timestamp()))
            
        if spoken_text:
            if not muted:
                say(spoken_text)
            else:
                print(spoken_text)

        if action_match:
            action_string = action_match.group(1)
            parts = [p.strip() for p in action_string.split("|")]
            action_type = parts[0]
            action_args = parts[1:]

            if action_type in TOOL_REGISTRY:
                target_function = TOOL_REGISTRY[action_type]
                success, message = target_function(*action_args)

                print(message)

                if not success:
                    error_msg = "I encountered an error trying to do that."
                    if not muted:
                        say(error_msg)
                    else:
                        print(error_msg)
            else:
                print(f"Unknown action requested: {action_type}")