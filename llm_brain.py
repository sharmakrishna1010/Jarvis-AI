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
                "content": f"You are my smart, casual, and highly capable AI best friend. Address me as '{callMe}'. Reply in 1-2 brief, conversational sentences using ONLY plain text (strictly no emojis, asterisks, or markdown). If my request requires opening an app or executing a system task, append the valid {operatingSystem} terminal command to the very end of your response exactly like this: COM_TO_RUN:command",
            },
            {"role": "user", "content": question},
        ],
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content
