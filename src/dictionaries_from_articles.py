import os
import ast
from typing import List, Dict

from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

from prompts.articles_to_dict import ARTICLE_TO_DICIONARY

def generate_article_dictionaries(prompt_template: str, blank_dict: dict, articles: List[str], llm) -> List[Dict]:
    """
    Uses an LLM to generate dictionaries from a list of articles, based on a structured prompt and blank dictionary.

    Args:
        prompt_template (str): Prompt template with a placeholder for the blank dictionary.
        blank_dict (dict): A sample dictionary structure to guide the output.
        articles (List[str]): List of article texts to process.

    Returns:
        List[Dict]: A list of dictionaries generated from the articles.
    """
    

    final_prompt = prompt_template.format(blank_claim_dict=blank_dict)
    system_message = SystemMessage(content=final_prompt)

    results = []

    for article_text in articles:
        human_message = HumanMessage(content=article_text)
        response = llm.invoke([system_message, human_message])

        try:
            parsed = ast.literal_eval(response.content)
            results.append(parsed)
        except Exception as e:
            print(f"Failed to parse response: {e}")

    return results