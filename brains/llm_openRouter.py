import os
from openrouter import OpenRouter
from dotenv import load_dotenv
from config.system_instruction import getSystemPrompt

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
                    "content": getSystemPrompt(question), 
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