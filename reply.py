from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()

def ask_gemma(query:str):
    genai.api_key = os.getenv("GENAI_API_KEY")  

    client = genai.Client()

    # grounding_tool = types.Tool(
    #     google_search=types.GoogleSearch()
    # )

    config = types.GenerateContentConfig(
        # tools = [grounding_tool],
        thinking_config=types.ThinkingConfig(thinking_level="low")
    )



    response = client.models.generate_content(
        model='gemini-3.1-flash-lite-preview',
        contents=query,
        config=config
    )


    return response.text
