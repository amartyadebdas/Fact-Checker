import os
import json
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from prompts.final_dictionary import FINAL_DICTIONARY
load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

def generate_final_dictionary(article_dictionaries, llm, prompt: str) -> str:
    """
    Takes a list of article dictionaries and an LLM instance, prepares messages,
    invokes the LLM to consolidate the dictionaries, and returns the
    content of the final consolidated dictionary.
    """
    # Prepare messages
    system_message = SystemMessage(content=prompt)
    human_message = HumanMessage(content=f"This the list of the dictionaries of articles{json.dumps(article_dictionaries, indent=2)}. Make sure the final dictionary is a dictionary with the appropriate keys with the values and nothing else.")

    # Get response
    response = llm.invoke([system_message, human_message])
    final_dict = response.content
    return final_dict