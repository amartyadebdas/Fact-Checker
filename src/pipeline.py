import os
from langchain_openai import ChatOpenAI
import pprint
pp = pprint.PrettyPrinter(indent=4)

from logger import logger 
from src.topic_dissection import dissect_topic
from src.disintegrate_claims import claim_disintegration
from src.claim_to_dict import generate_claim_dict
from src.keywords_from_claim import generate_keywords
from src.articles_from_keywords import fetch_articles_from_keywords
from src.generate_blank_dict import generate_blank_dict
from src.dictionaries_from_articles import generate_article_dictionaries
from src.final_dict import generate_final_dictionary
from src.compare import compare_claim_with_evidence

# Import all your prompts.
from prompts.topic_dissection import DISSECT_TOPIC
from prompts.claim_dict import CLAIM_TO_DICTIONARY
from prompts.keywords import GENERATE_KEYWORDS
from prompts.blank_dictionary import BLANK_DICTIONARY
from prompts.articles_to_dict import ARTICLE_TO_DICTIONARY
from prompts.final_dictionary import FINAL_DICTIONARY
from prompts.claim_vs_evidence import CLAIM_VS_EVIDENCE
from prompts.claim_dissect import DISSECT_CLAIM

def process_claims(claim: str,articles, llm_instance: ChatOpenAI): # Added type hint for clarity
    """
    Processes a single claim through the verification pipeline and returns a dictionary
    containing the evidence and confidence score.
    """
    logger.info(f"--- Processing Claim: '{claim}' ---")

    # Step 1: Generate claim dictionary
    logger.info("Generating claim dictionary...")
    claim_dict = generate_claim_dict(claim, llm_instance, CLAIM_TO_DICTIONARY) 
    # print(claim_dict)

    logger.debug("Claim Dictionary:\n%s", claim_dict)
    logger.info("Claim dictionary generated.")

    # Step 2: Generate blank dictionary
    logger.info("Generating blank dictionary...")
    blank_dict = generate_blank_dict(BLANK_DICTIONARY, claim_dict, llm_instance) 
    logger.info("Blank dictionary generated.")

    # Step 3: Generate article dictionaries
    logger.info("Generating article dictionaries...")
    article_dictionaries = generate_article_dictionaries(ARTICLE_TO_DICTIONARY, blank_dict, articles, llm_instance)
    logger.info("Number of article dictionaries generated: %d", len(article_dictionaries))

    # Step 4: Generate final dictionary
    logger.info("Generating final dictionary...")
    final_dict = generate_final_dictionary(article_dictionaries, llm_instance, FINAL_DICTIONARY) 
    logger.debug("Final Dictionary:\n%s",final_dict )
    print(final_dict)
    logger.info("Final dictionary generated.")

    # Step 5: Compare claim with evidence
    logger.info("Comparing claim with evidence...")
    comparison_result = compare_claim_with_evidence(claim_dict, final_dict, llm_instance, CLAIM_VS_EVIDENCE) 
    logger.info("Comparison completed.")
    
    return comparison_result

def main(user_input: str, llm_instance: ChatOpenAI): # Added type hint for clarity
    """
    Takes user input, disintegrates claims, and processes each claim.
    """

    all_results = {}
    topics = dissect_topic(user_input, DISSECT_TOPIC,llm_instance)
    logger.info(f"Total topics: {len(topics)}")
    for topic in topics:
        logger.info("Generating Keywords...")
        try:    
            keywords = generate_keywords(topic, GENERATE_KEYWORDS, llm_instance)
            logger.info("Successfully generated keywords...")
        except Exception as e:
            logger.exception("Failed to generate keywords...:%s", str(e))
        logger.info("Generating articles from the keywords...")
        try:
            articles = fetch_articles_from_keywords(keywords)
            if (len(articles))==0:
                logger.warning("No articles generated.")
            else:
                logger.info(f"Article generated successful. Total article generated : {len(articles)}")
        except Exception as e:
            logger.exception("Article generation failed...:%s", str(e))
        logger.info("Dissecting claims...")
        try:
            claims = claim_disintegration(topic, DISSECT_CLAIM, llm_instance)
            logger.info(f"Claim generation successful. Total claims: {len(claims)}")
        except Exception as e:
            logger.exception("Claim extraction failed...:%s", str(e))
        if len(claims) == 1:
            result = process_claims(claims[0],articles,llm_instance) 
            all_results[claims[0]] = result
        elif len(claims) > 1:
            for i, claim in enumerate(claims):
                logger.info(f"--- Processing Claim {i+1}: '{claim}' ---")
                result = process_claims(claim, articles, llm_instance) 
                all_results[claim] = result
        else:
            logger.warning("No claims found in the input.")

    return all_results

if __name__ == "__main__":
    user_input = input("Please provide me with one or more claims to analyze:\n")
    results = main(user_input, llm) 

    logger.info("\n--- Overall Results ---")
    for claim, result in results.items():
        logger.info(f"Claim: {claim}")
        logger.info(f"Evidence: {result}")
        logger.info("-" * 20)