import os
from langchain_core.prompts import ChatPromptTemplate


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

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ('system',prompt),
            ('human','{input}')
        ]
    )
    chain = final_prompt |llm

    response = chain.invoke({
        'input':"Generate the response in such a way that shows where the claim doesn't match the evidence in English Natural Language.",
        'claim_dictionary':claim_dict,
        'evidence_dictionary':evidence_dict

    })
    return response.content