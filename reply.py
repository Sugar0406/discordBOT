from google import genai
import os
from google.genai import types


# load_dotenv()

# async def ask_gemma_async(query: str) -> str:
#     loop = asyncio.get_running_loop()

#     def sync_call():
#         genai.api_key = os.getenv("GENAI_API_KEY")
#         client = genai.Client()
#         config = types.GenerateContentConfig(
#             thinking_config=types.ThinkingConfig(thinking_level="low")
#         )
#         response = client.models.generate_content(
#             model='gemini-3.1-flash-lite-preview',
#             contents=query,
#             config=config
#         )
#         return response.text

#     return await loop.run_in_executor(None, sync_call)



def ask_gemma(query:str):
    genai.api_key = os.getenv("GENAI_API_KEY")  

    client = genai.Client()

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    )

    response = client.models.generate_content(
        model='gemini-3.1-flash-lite-preview',
        contents=query,
        config=config
    )


    return response.text
