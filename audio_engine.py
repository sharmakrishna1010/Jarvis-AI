import sounddevice as sd
import speech_recognition as sr
import torch
from kokoro import KPipeline

# Initialize the Kokoro Pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Loading Voice Models on: {device.upper()}...")
pipeline = KPipeline(lang_code="a", device=device)


def say(text):
    """Generates audio from text and plays it instantly in memory."""
    generator = pipeline(text, voice="af_heart", speed=1)
    # generator = pipeline(text, voice='af_nicole', speed=1)

    for i, (gs, ps, audio) in enumerate(generator):
        sd.play(audio, samplerate=24000)
        sd.wait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.energy_threshold = 100
        recognizer.pause_threshold = 1
        recognizer.dynamic_energy_threshold = True

        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Network error with the speech recognition service.")
        return ""
