from audio_engine import listen, say
from action import performAction , greetings

if __name__ == "__main__":

    greetings()
    while True:
        task = listen()
        performAction(task)