from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


load_dotenv()
openai_chat_model = ChatOpenAI(model="gpt-4")
openai_model = OpenAI(model="gpt-4")
