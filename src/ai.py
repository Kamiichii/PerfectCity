import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
_client: genai.Client |None=None
system_prompt = "The user will imput a city they want to learn more about.Give them a short explanation of the city prioritizing weather and natural attributes"

def get_client():
    global _client
    if _client is None:
        api_key = os.environ["GEMINI_API_KEY"]
        _client = genai.Client(api_key=api_key)
    return _client

def use_ai(question):
    client = get_client()
    content = input(question)
    messages = [
    types.Content(role="user", parts=[types.Part(text=content)]),
    ]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages,config=types.GenerateContentConfig(system_instruction=system_prompt))
    print(response.text)
