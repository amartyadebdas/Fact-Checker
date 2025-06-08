import ast
from typing import List, Dict
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def generate_article_dictionaries(prompt_template: str, blank_dict: str, articles, llm:ChatOpenAI) -> List[Dict]:
    """
    Uses an LLM to generate dictionaries from a list of articles, based on a structured prompt and blank dictionary.

    Args:
        prompt_template (str): Prompt template with a placeholder for the blank dictionary.
        blank_dict (dict): A sample dictionary structure to guide the output.
        articles (List[str]): List of article texts to process.

    Returns:
        List[Dict]: A list of dictionaries generated from the articles.
    """

    final_prompt = ChatPromptTemplate.from_messages([
        ('system',prompt_template),
        ('human',"{input}")
    ])

    results = []

    for article_text in articles:
        chain = final_prompt | llm
        response = chain.invoke({
            'blank_claim_dict':blank_dict,
            "input": article_text
        })

        try:
            parsed = ast.literal_eval(response.content)
            results.append(parsed)
        except Exception as e:
            print(f"Failed to parse response: {e}")

    return results

