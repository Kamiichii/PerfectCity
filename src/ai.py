import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
_client: genai.Client |None=None
_messages = []


def get_client():
    global _client
    if _client is None:
        api_key = os.environ["GEMINI_API_KEY"]
        _client = genai.Client(api_key=api_key)
    return _client
def create_system_prompt(final_list): 
    return f"You will be given a list of 10 cities and the user will ask about one of them give them a short description of the city prioritizing physical and population attributes. If the number or city is not given in the list ask the user to select a city from the list but answer any other question about the city.Here is the top 10 list: {final_list}"

def use_ai(user_input,system_prompt):
    client = get_client()
    global _messages
    content = user_input
    _messages += [
    types.Content(role="user", parts=[types.Part(text=content)]),
    ]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=_messages,config=types.GenerateContentConfig(system_instruction=system_prompt))
    _messages += [
    types.Content(role="model", parts=[types.Part(text=response.text)]),
    ]
    print(response.text)
