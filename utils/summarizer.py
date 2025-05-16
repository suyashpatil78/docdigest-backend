from openai import OpenAI
import os
from dotenv import load_dotenv
from utils.prompt import PDF_PROMPT, CHAT_PROMPT
from google import genai
from google.genai import types

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_with_gpt(text):
    response = client.responses.create(
      model="gpt-4o",
      instructions=PROMPT,
      input=text,
    )
    return response.output_text

def summarize_with_gemini(text):
    response = gemini_client.models.generate_content(
      model="gemini-2.0-flash",
      config=types.GenerateContentConfig(
        system_instruction=PDF_PROMPT
      ),
      contents=text
    )
    return response.text

def chat_with_gemini(text, question):
    response = gemini_client.models.generate_content(
      model="gemini-2.0-flash",
      config=types.GenerateContentConfig(
        system_instruction=CHAT_PROMPT
      ),
      contents=(text + '\n\n' + question)
    )
    return response.text