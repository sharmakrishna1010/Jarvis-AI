import os
import datetime
import webbrowser
from audio_engine import say
from sites import siteList

def greetings():
    now = datetime.datetime.now()
    if now.hour < 12:
        say("Good Morning sir")
    elif now.hour < 18:
        say("Good Afternoon sir")
    else:
        say("Good Evening sir")

def performAction(task):
    if (task):
        if "open code" in task.lower():
            os.system("start code")
            say("Opening Visual Studio Code")
        elif "open browser" in task.lower():
            webbrowser.open("google.com")
            say("Opening browser")
        elif "current time" in task.lower():
            now = datetime.datetime.now()
            say(f"Sir, the time is {now.hour}:{now.minute}")
        elif "today's date" in task.lower():
            now = datetime.datetime.now()
            say(f"Sir, today's date is {now.day}/{now.month}/{now.year}")
        elif "exit" in task.lower():
            say("Goodbye")
            exit()
        else:
            for site in siteList:
                if site[0] in task.lower():
                    webbrowser.open(site[1])
                    say(f"Opening {site[0]} sir")
                    break