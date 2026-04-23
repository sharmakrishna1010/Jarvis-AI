import time
from llm_mistral import askMistral
from llm_gemini import askGemini

def askJarvis(question):
    print("Thinking (via Gemini)...")
    try:
        answer = askGemini(question)
        return answer
        
    except Exception as e:
        error_msg = str(e).lower()
        if "quota" in error_msg or "demand" in error_msg or "503" in error_msg or "429" in error_msg:
            print("Gemini is experiencing high demand. Seamlessly swapping to Mistral...")
        else:
            print(f"Gemini hit an error: {e}. Swapping to Mistral...")
            
        try:
            answer = askMistral(question)
            return answer
        except Exception as e2:
            print(f"Total brain failure. Both models are down. Error: {e2}")
            return None