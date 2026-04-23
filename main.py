from audio_engine import listen, say
from action import performAction , greetings

if __name__ == "__main__":

    greetings()
    while True:
        task = listen()
        if "exit" in task.lower():
            say("Goodbye sir!")
            break
        elif "shutdown" in task.lower():
            say("Goodbye sir!")
            break
        performAction(task)