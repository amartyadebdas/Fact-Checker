import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from prompts.claim_vs_evidence import CLAIM_VS_EVIDENCE

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

def compare_claim_with_evidence(claim_dict: dict, evidence_dict: dict, llm, prompt) -> str:
    """
    Compares a claim dictionary with an evidence dictionary using a language model.

    Args:
        claim_dict (dict): The claim dictionary to compare.
        evidence_dict (dict): The evidence dictionary to compare against.
        llm: The language model instance to use for comparison.
        prompt (str): The prompt to guide the comparison.

    Returns:
        str: The response from the language model comparing the two dictionaries.
    """
    system_message = SystemMessage(content=prompt.format(claim_dictionary=claim_dict, evidence_dictionary=evidence_dict))
    human_message = HumanMessage(content="Generate the response in such a way that shows where the claim doesn't match the evidence in English Natural Language.")
    
    response = llm.invoke([system_message, human_message])
    return response.content