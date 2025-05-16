import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

load_dotenv()

def generate_claim_dict(user_input: str, llm, prompt:str) -> dict:
    """
    Uses a language model to generate a claim dictionary from the given article using the provided prompt.

    Args:
        prompt (str): The system prompt guiding the transformation.
        article (str): The article content to transform.

    Returns:
        dict: A dictionary parsed from the language model's response.
    """

    system_message = SystemMessage(content=prompt)
    human_message = HumanMessage(content=user_input)

    response = llm.invoke([system_message, human_message])
    return response.content