import os
from langchain_core.prompts import ChatPromptTemplate

def generate_blank_dict(prompt_template: str, claim_dictionary: dict, llm) -> dict:
    """
    Uses a language model to generate a blank dictionary from the given claim dictionary using the provided prompt.

    Args:
        prompt_template (str): The system prompt guiding the transformation.
        claim_dict (dict): The claim dictionary to transform.

    Returns:
        dict: A dictionary parsed from the language model's response.
    """

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ('system', prompt_template),
            ('human','{input}')
        ]
    )
    chain = final_prompt | llm

    response = chain.invoke({
        'input':claim_dictionary
    })

    response = response.content.replace('json','')
    response = response.replace('python','')
    return response

