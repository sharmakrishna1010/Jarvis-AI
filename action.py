import os
import datetime
import webbrowser
import subprocess
from audio_engine import say
from sites import siteList
from llm_brain import askMistral
from userPref import userName, callMe


def is_safe_command(command):
    """Scans the command for dangerous Windows/PowerShell operations."""
    
    dangerous_keywords = {
        "del", "erase", "rmdir", "rm", "format", "diskpart", 
        "reg", "shutdown", "restart", "remove-item", "clear-content", 
        "drop", "truncate", "attrib", "icacls", "takeown"
    }
    
    words = command.lower().split()
    
    for word in words:
        if word in dangerous_keywords:
            return False
            
    if "|" in command or "&&" in command or ";" in command:
        return False
        
    return True

def greetings():
    now = datetime.datetime.now()
    if now.hour < 12:
        say(f"Good Morning {userName} {callMe}, how can I help you?")
    elif now.hour < 18:
        say(f"Good Afternoon {userName} {callMe}, how can I help you?")
    else:
        say(f"Good Evening {userName} {callMe}, how can I help you?")

def performAction(task):
    if task:
        if "open" in task.lower() and any(site[0] in task.lower() for site in siteList):
            for site in siteList:
                if site[0] in task.lower():
                    webbrowser.open(site[1])
                    say("Opening " + site[0] + " for you.")
                    break
                    
        elif "current time" in task.lower():
            now = datetime.datetime.now()
            say("The current time is " + now.strftime("%I:%M %p"))
            
        elif "today's date" in task.lower():
            now = datetime.datetime.now()
            say("Today's date is " + now.strftime("%B %d, %Y")) 
            
        else:
            answer = askMistral(task.lower())
            
            if answer:
                if "COM_TO_RUN:**" in answer:
                    parts = answer.split("COM_TO_RUN:**")
                    spoken_text = parts[0].strip()
                    command_string = parts[1].strip()
                    
                    command_to_run = command_string.replace("**", "").replace("'", "")
                    
                    if not is_safe_command(command_to_run):
                        print(f"SECURITY ALERT: Blocked dangerous command -> {command_to_run}")
                        say("I am sorry, but that command violates my core security protocols. I will not execute it.")
                        return
                    
                    if spoken_text:
                        say(spoken_text)
                    
                    print(f"Executing System Command: {command_to_run}")
                    try:
                        subprocess.Popen(command_to_run, shell=True)
                    except Exception as e:
                        print(f"Failed to run command: {e}")
                        say("I encountered an error trying to execute that command.")
                        
                else:
                    say(answer)
            else:
                say("Unable to answer your question, please try again.")