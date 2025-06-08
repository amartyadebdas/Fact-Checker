import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from prompts.claim_dict import CLAIM_TO_DICTIONARY
load_dotenv()

api_key = os.environ['OPENAI_API_KEYY']
llm = ChatOpenAI(model = 'gpt-4o-mini', api_key=api_key)

def generate_claim_dict(user_input: str, llm, prompt:str) -> dict:
    """
    Uses a language model to generate a claim dictionary from the given article using the provided prompt.

    Args:
        prompt (str): The system prompt guiding the transformation.
        article (str): The article content to transform.

    Returns:
        dict: A dictionary parsed from the language model's response.
    """

    final_prompt = ChatPromptTemplate.from_messages([
        ('system', prompt),
        ('human',"{input}")
    ])

    chain = final_prompt | llm

    response = chain.invoke({
        'input': user_input
    })

    response  = response.content.replace("python","")
    return response