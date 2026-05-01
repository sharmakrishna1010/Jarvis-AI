import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from system_instruction import getSystemPrompt
load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def askGemini(question):
    system_prompt = getSystemPrompt(question)

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.5,
        )
    )

    print(response.text)
    return response.text