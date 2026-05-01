import time
from brains.llm_mistral import askMistral
from brains.llm_gemini import askGemini
from brains.llm_openRouter import askOpenRouter


def askJarvis(question):
    try:
        print("Thinking (via Gemini)...")
        answer = askGemini(question)
        if answer:
            return answer
    except Exception as e:
        print(f"Gemini failed. Falling back to OpenRouter...")

    try:
        print("Thinking (via Mistral)...")
        answer = askMistral(question)
        if answer:
            return answer
    except Exception as e:
        print(f"Mistral failed. Falling back to OpenRouter...")

    try:
        print("Thinking (via OpenRouter)...")
        answer = askOpenRouter(question)
        if answer:
            return answer
    except Exception as e:
        print(f"Total brain failure. All API endpoints are down! Error: {e}")

    return "I am currently experiencing a critical server failure and cannot process that request."
