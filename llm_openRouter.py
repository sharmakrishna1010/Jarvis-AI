import os
from openrouter import OpenRouter
from dotenv import load_dotenv
from system_instruction import systemInstruction

load_dotenv()

# OpenRouter SDK setup
client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))

def askOpenRouter(question):
    print("Thinking (via OpenRouter)...")
    try:
        response = client.chat.send(
            model="minimax/minimax-m2", 
            messages=[
                {
                    "role": "system",
                    "content": f"{systemInstruction}", 
                },
                {"role": "user", "content": question},
            ],
            temperature=0.1,   
        )

        answer = response.choices[0].message.content
        return answer
        
    except Exception as e:
        print(f"OpenRouter hit an error: {e}")
        return None