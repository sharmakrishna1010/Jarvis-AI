import speech_recognition as sr
import os

def say(text):
    os.system('say ' + text)

if __name__ == '__main__':
    print('Hello World!')
    say('Hello World!')

