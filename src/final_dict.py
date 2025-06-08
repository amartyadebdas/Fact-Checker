import os
import json
from langchain_core.prompts import ChatPromptTemplate


def generate_final_dictionary(article_dictionaries, llm, prompt: str) -> str:
    """
    Takes a list of article dictionaries and an LLM instance, prepares messages,
    invokes the LLM to consolidate the dictionaries, and returns the
    content of the final consolidated dictionary.
    """
    # Prepare messages
    final_prompt = ChatPromptTemplate.from_messages([
        ('system', prompt),
        ('human',"{input}")
    ])

    chain = final_prompt | llm
    # Get response

    response = chain.invoke({
        'input':json.dumps(article_dictionaries, indent=2)
    })

    final_dict = response.content
    return final_dict