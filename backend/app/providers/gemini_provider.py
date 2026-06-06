import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiProvider:

    @staticmethod
    def generate(prompt: str) -> str:

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f'''
{{
    "main_tf": "",
    "variables_tf": "",
    "outputs_tf": "",
    "error": "{str(e)}"
}}
'''
