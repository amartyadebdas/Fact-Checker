import os
from dotenv import load_dotenv

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from prompts.blank_dictionary import BLANK_DICTIONARY

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

def generate_blank_dict(prompt_template: str, claim_dictionary: dict, llm) -> dict:
    """
    Uses a language model to generate a blank dictionary from the given claim dictionary using the provided prompt.

    Args:
        prompt_template (str): The system prompt guiding the transformation.
        claim_dict (dict): The claim dictionary to transform.

    Returns:
        dict: A dictionary parsed from the language model's response.
    """
    
    system_message = SystemMessage(content=prompt_template)
    human_message = HumanMessage(content=f"{claim_dictionary}")

    response = llm.invoke([system_message, human_message])
    return response.content