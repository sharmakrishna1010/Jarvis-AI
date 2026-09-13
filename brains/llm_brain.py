import time
from brains.llm_mistral import askMistral
from brains.llm_gemini import askGemini
from brains.llm_openRouter import askOpenRouter


def askJarvis(question, chat_context=""):
    try:
        print("Thinking (via Gemini)...")
        answer = askGemini(question, chat_context, model="gemini-3.5-flash")
        if answer:
            return answer
    except Exception as e:
        print(f"Gemini 3.5 flash failed. Falling back to Mistral...\nError: {e}\n")

    try:
        print("Thinking (via Mistral)...")
        answer = askMistral(question, chat_context)
        if answer:
            return answer
    except Exception as e:
        print(f"Mistral failed. Falling back to OpenRouter...\nError: {e}\n")

    try:
        print("Thinking (via Gemini)...")
        answer = askGemini(question, chat_context, model="gemini-3.5-flash-lite")
        if answer:
            return answer
    except Exception as e:
        print(f"Gemini 3.5 flash lite failed. Falling back to OpenRouter...\nError: {e}\n")

    try:
        print("Thinking (via OpenRouter)...")
        answer = askOpenRouter(question, chat_context)
        if answer:
            return answer
    except Exception as e:
        print(f"Total brain failure. All API endpoints are down! Error: {e}")

    return "I am currently experiencing a critical server failure and cannot process that request."
