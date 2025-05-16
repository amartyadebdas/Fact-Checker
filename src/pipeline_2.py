import os
from dotenv import load_dotenv
load_dotenv()

from src.disintegrate_claims import claim_disintegration
from src.claim_to_dict import generate_claim_dict
from src.keywords_from_claim import generate_keywords
from src.articles_from_keywords import fetch_articles_from_keywords
from src.generate_blank_dict import generate_blank_dict
from src.dictionaries_from_articles import generate_article_dictionaries
from src.final_dict import generate_final_dictionary
from src.compare import compare_claim_with_evidence

from prompts.claim_dict import CLAIM_TO_DICTIONARY
from prompts.keywords import GENERATE_KEYWORDS

from prompts.blank_dictionary import BLANK_DICTIONARY
from prompts.articles_to_dict import ARTICLE_TO_DICIONARY
from prompts.final_dictionary import FINAL_DICTIONARY
from prompts.claim_vs_evidence import CLAIM_VS_EVIDENCE
from prompts.claim_dissect import DISSECT_CLAIM



openai_api_key = os.environ.get("OPENAI_API_KEY")
from langchain_openai.chat_models import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)


def pipeline(claim: str, llm_instance: ChatOpenAI) -> dict:
    """
    Processes a single claim through the verification pipeline and returns a dictionary
    containing the evidence and confidence score.
    """
    print(f"\n--- Processing Claim: '{claim}' ---")

    #step 1: Generate claim dictionary
    print("Generating claim dictionary...")
    claim_dict = generate_claim_dict(claim, llm_instance, CLAIM_TO_DICTIONARY)
    print(claim_dict)
    print("Claim dictionary generated.")

    # step 2: Generate keywords
    print("Generating keywords...")
    keywords = generate_keywords(claim, GENERATE_KEYWORDS, llm_instance)
    print(keywords)
    print("Keywords generated.")
    # step 3: Fetch articles
    print("Fetching articles...")
    articles = fetch_articles_from_keywords(keywords)
    print("Articles fetched.")
    # step 4: generate blank dictionary
    print("Generating blank dictionary...")
    blank_dict = generate_blank_dict(BLANK_DICTIONARY, claim_dict, llm_instance)
    print("Blank dictionary generated.")
    # step 5: Generate article dictionaries
    print("Generating article dictionaries...")
    article_dictionaries = generate_article_dictionaries(ARTICLE_TO_DICIONARY, blank_dict, articles, llm_instance)
    print("Article dictionaries generated.")
    # step 6: Generate final dictionary
    print("Generating final dictionary...")
    final_dict = generate_final_dictionary(article_dictionaries, llm_instance, FINAL_DICTIONARY)
    print(final_dict)
    print("Final dictionary generated.")
    # step 7: Compare claim with evidence
    print("Comparing claim with evidence...")
    comparison_result = compare_claim_with_evidence(claim_dict, final_dict, llm_instance, CLAIM_VS_EVIDENCE)
    print("Comparison completed.")
    return comparison_result


def main(user_input: str, llm_instance: ChatOpenAI):
    """
    Takes user input, disintegrates claims, and processes each claim.
    """
    claims = claim_disintegration(user_input, DISSECT_CLAIM, llm_instance)
    all_results = {}

    print("Number of claims found:", len(claims))
    print("Claims found:", claims)

    if len(claims) == 1:
        result = pipeline(claims[0], llm_instance)
        all_results[claims[0]] = result
    elif len(claims) > 1:
        
        for i, claim in enumerate(claims):
            print(f"\n--- Processing Claim {i+1}: '{claim}' ---")
            result = pipeline(claim, llm_instance)
            all_results[claim] = result
    else:
        print("No claims found in the input.")

    return all_results

if __name__ == "__main__":
    user_input = input("Please provide me with one or more claims to analyze:\n")
    results = main(user_input, llm)
    print("\n--- Overall Results ---")
    for claim, result in results.items():
        print(f"Claim: {claim}")
        print(f"Evidence: {result}")
        print("-" * 20)