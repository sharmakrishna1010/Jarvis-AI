import re
from audio_engine import say
from llm_brain import askMistral
from registry import TOOL_REGISTRY
from userPref import userName, callMe 
import datetime

def greetings():
    currentTime = datetime.datetime.now().strftime("%H:%M")
    if int(currentTime[:2]) < 12:
        say(f"Good morning {userName} {callMe}! How can I help you today?")
    elif int(currentTime[:2]) < 18:
        say(f"Good afternoon {userName} {callMe}! How can I help you today?")
    else:
        say(f"Good evening {userName} {callMe}! How can I help you today?")

def performAction(task):
    if not task:
        return

    answer = askMistral(task.lower())

    if answer:
        # Check if the LLM decided to use a tool
        action_match = re.search(r'\[ACTION:\s*(.*?)\s*\]', answer, re.DOTALL)

        if action_match:
            action_string = action_match.group(1)
            parts = [p.strip() for p in action_string.split('|')]
            action_type = parts[0]      
            action_args = parts[1:]    

            # Speak any conversational text
            spoken_text = answer.replace(action_match.group(0), "").strip()
            if spoken_text: say(spoken_text)

            # THE DISPATCHER 
            if action_type in TOOL_REGISTRY:
                target_function = TOOL_REGISTRY[action_type]
                
                
                success, message = target_function(*action_args)
                
                print(message)
                if not success:
                    say("I encountered an error trying to do that.")
            else:
                print(f"Unknown action requested: {action_type}")
                
        else:
            say(answer)