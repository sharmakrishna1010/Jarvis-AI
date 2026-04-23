import os
from mistralai.client import Mistral
from dotenv import load_dotenv
from userPref import callMe, operatingSystem

load_dotenv()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])


def askMistral(question):
    response = client.chat.complete(
        model="open-mistral-7b",
        messages=[
            {
                "role": "system",
                "content": f"You are my smart, casual, and highly capable female AI best friend. Address me as '{callMe}'. Reply in 1-2 brief, conversational sentences using ONLY plain text. IMPORTANT: ONLY append a 'COM_TO_RUN:command' if I explicitly ask you to open an application, launch a program, or manage the system. Do NOT generate commands for conversational replies, jokes, or to confirm you did something. Never use 'echo'. Operating System: {operatingSystem}.",
            },
            {"role": "user", "content": question},
        ],
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content
