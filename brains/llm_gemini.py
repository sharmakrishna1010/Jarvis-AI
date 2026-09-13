import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config.system_instruction import getSystemPrompt
load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def askGemini(question , chat_context="", model="gemini-3.5-flash-lite"):
    system_prompt = getSystemPrompt(question , chat_context)

    response = client.models.generate_content(
        model=model, 
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.5,
            max_output_tokens=500,
        )
    )

    print(response.text)
    return response.text