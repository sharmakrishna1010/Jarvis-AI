import os
from mistralai.client import Mistral
from dotenv import load_dotenv
from system_instruction import getSystemPrompt

load_dotenv()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])


def askMistral(question):
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "system",
                "content": getSystemPrompt(question),
            },
            {"role": "user", "content": question},
        ],
        temperature=0.1,
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content
