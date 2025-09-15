from config import set_environment
set_environment()

from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI

openai_llm = OpenAI()

gemini_pro = GoogleGenerativeAI(model = "gemini-1.5-pro")

response = openai_llm.invoke("Tell me a joke about light bulbs!")
print(response)