from openai import OpenAI
import os
from dotenv import load_dotenv
from utils.prompt import PROMPT

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_with_gpt(text):
    response = client.responses.create(
      model="gpt-4o",
      instructions=PROMPT,
      input=text,
    )
    return response.output_text