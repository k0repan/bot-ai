from dotenv import load_dotenv
from os import getenv
from openai import OpenAI
load_dotenv()


class AI_Api:

    def __init__(self, content: str, max_tokens: int):
        self.client = OpenAI(api_key=getenv("API_KEY"))
        self.content: str = content
        self.max_tokens: int = max_tokens

    def search(self, query: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {'role': 'system', 'content': self.content},
                {'role': 'user', 'content': query}
            ]
        )

        return response.choices[0].message.content
