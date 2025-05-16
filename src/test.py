from dotenv import load_dotenv
load_dotenv()

from langchain_openai.chat_models import ChatOpenAI
import os
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.environ.get("OPENAI_API_KEY"))

print(llm.invoke("Hi").content)