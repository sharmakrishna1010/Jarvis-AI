import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

from system_instruction import systemInstruction
def askGemini(question):
    system_prompt = systemInstruction

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7, # 0.7 makes her sound a bit more casual and human
        )
    )

    print(response.text)
    return response.text