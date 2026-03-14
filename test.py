from google import genai
from google.genai.types import (
    GenerateContentConfig,
    GoogleSearch,
    HttpOptions,
    Tool,
)
import os 
from dotenv import load_dotenv


load_dotenv()

genai.api_key = os.getenv("GENAI_API_KEY")
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="When is the next total solar eclipse in the United States?",
    config=GenerateContentConfig(
        tools=[
            # Use Google Search Tool
            Tool(
                google_search=GoogleSearch()
            )
        ],
    ),
)