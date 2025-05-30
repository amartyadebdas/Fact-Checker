# import os
# from dotenv import load_dotenv
# load_dotenv()

# from src.logger import logger
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# from src.disintegrate_claims import claim_disintegration
# from src.claim_to_dict import generate_claim_dict
# from src.keywords_from_claim import generate_keywords
# from src.articles_from_keywords import fetch_articles_from_keywords
# from src.generate_blank_dict import generate_blank_dict
# from src.dictionaries_from_articles import generate_article_dictionaries
# from src.final_dict import generate_final_dictionary
# from src.compare import compare_claim_with_evidence

# from prompts.claim_dict import CLAIM_TO_DICTIONARY
# from prompts.keywords import GENERATE_KEYWORDS

# from prompts.blank_dictionary import BLANK_DICTIONARY
# from prompts.articles_to_dict import ARTICLE_TO_DICIONARY
# from prompts.final_dictionary import FINAL_DICTIONARY
# from prompts.claim_vs_evidence import CLAIM_VS_EVIDENCE
# from prompts.claim_dissect import DISSECT_CLAIM



# openai_api_key = os.environ.get("OPENAI_API_KEY")
# from langchain_openai.chat_models import ChatOpenAI
# llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)


# def pipeline(claim: str, llm_instance: ChatOpenAI) -> dict:
#     """
#     Processes a single claim through the verification pipeline and returns a dictionary
#     containing the evidence and confidence score.
#     """
#     # print(f"\n--- Processing Claim: '{claim}' ---")
#     logger.info("---Processing Claim---")

#     #step 1: Generate claim dictionary
#     print("---Generating claim dictionary---")
#     claim_dict = generate_claim_dict(claim, llm_instance, CLAIM_TO_DICTIONARY)
#     print("Claim Dictionary:\n",claim_dict)
#     logger.debug("Claim Dictionary:\n%s", pp.pformat(claim_dict))
#     logger.info("===Claim dictionary generated.===")

#     # step 2: Generate keywords
#     logger.info("---Generating keywords---")
#     keywords = generate_keywords(claim, GENERATE_KEYWORDS, llm_instance)
#     print(keywords)
#     logger.info("===Keywords Generated.===")
#     # step 3: Fetch articles
#     logger.info("---Fetching Articles---")
#     articles = fetch_articles_from_keywords(keywords)
#     logger.info("===Articles fetched.===")
#     # step 4: generate blank dictionary
#     logger.info("---Generating Blank Dictionary---")
#     blank_dict = generate_blank_dict(BLANK_DICTIONARY, claim_dict, llm_instance)
#     print("Blank Dictionary: \n", blank_dict)
#     logger.debug("Blank Dictionary:\n%s", pp.pformat(blank_dict))
#     print("===Blank dictionary generated.===")
#     # step 5: Generate article dictionaries
#     print("---Generating article dictionaries---")
#     article_dictionaries = generate_article_dictionaries(ARTICLE_TO_DICIONARY, blank_dict, articles, llm_instance)
#     print("===Article dictionaries generated.===")
#     # step 6: Generate final dictionary
#     logger.info("---Generating Final Dictionary---")
#     final_dict = generate_final_dictionary(article_dictionaries, llm_instance, FINAL_DICTIONARY)
#     print("Final Dictionary: \n", final_dict)
#     logger.debug("Final Dictionary:\n%s", pp.pformat(final_dict))
#     logger.info("===Final dictionary generated===")
#     # step 7: Compare claim with evidence
#     logger.info("---Comparing claim with evidence---")
#     comparison_result = compare_claim_with_evidence(claim_dict, final_dict, llm_instance, CLAIM_VS_EVIDENCE)
#     logger.info("===Comparison completed===")

#     return comparison_result


# def main(user_input: str, llm_instance: ChatOpenAI):
#     """
#     Takes user input, disintegrates claims, and processes each claim.
#     """
#     claims = claim_disintegration(user_input, DISSECT_CLAIM, llm_instance)
#     all_results = {}

#     print("Number of claims found:", len(claims))
#     print("Claims found:", claims)

#     if len(claims) == 1:
#         result = pipeline(claims[0], llm_instance)
#         all_results[claims[0]] = result
#     elif len(claims) > 1:
        
#         for i, claim in enumerate(claims):
#             print(f"\n--- Processing Claim {i+1}: '{claim}' ---")
#             result = pipeline(claim, llm_instance)
#             all_results[claim] = result
#     else:
#         print("No claims found in the input.")

#     return all_results

# if __name__ == "__main__":
#     user_input = input("Please provide me with one or more claims to analyze:\n")
#     results = main(user_input, llm)
#     print("\n--- Overall Results ---")
#     for claim, result in results.items():
#         print(f"Claim: {claim}")
#         print(f"Evidence: {result}")
#         print("-" * 20)

import os
from dotenv import load_dotenv
load_dotenv()

import pprint
pp = pprint.PrettyPrinter(indent=4)

# MLflow imports
import mlflow
from src.logger import logger # Assuming 'logger' is correctly configured

# Import all your custom modules/functions.
from src.disintegrate_claims import claim_disintegration
from src.claim_to_dict import generate_claim_dict
from src.keywords_from_claim import generate_keywords
from src.articles_from_keywords import fetch_articles_from_keywords
from src.generate_blank_dict import generate_blank_dict
from src.dictionaries_from_articles import generate_article_dictionaries
from src.final_dict import generate_final_dictionary
from src.compare import compare_claim_with_evidence

# Import all your prompts.
from prompts.claim_dict import CLAIM_TO_DICTIONARY
from prompts.keywords import GENERATE_KEYWORDS
from prompts.blank_dictionary import BLANK_DICTIONARY
from prompts.articles_to_dict import ARTICLE_TO_DICIONARY
from prompts.final_dictionary import FINAL_DICTIONARY
from prompts.claim_vs_evidence import CLAIM_VS_EVIDENCE
from prompts.claim_dissect import DISSECT_CLAIM

# --- LLM Setup ---
# You've commented out the ChatGoogleGenerativeAI and are using ChatOpenAI.
# I'll stick with ChatOpenAI as per your latest code.
openai_api_key = os.environ.get("OPENAI_API_KEY")
from langchain_openai.chat_models import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

# --- Helper function to log prompts as artifacts ---
# def _log_prompt_as_artifact(prompt_name: str, prompt_content: str):
#     """Logs a prompt string as a .txt file artifact in MLflow."""
#     try:
#         # Create a temporary file to save the prompt content
#         file_name = f"prompt_{prompt_name.lower()}.txt"
#         with open(file_name, "w") as f:
#             f.write(prompt_content)
#         mlflow.log_artifact(file_name, artifact_path="prompts")
#         os.remove(file_name) # Clean up the temporary file
#         logger.info(f"Logged prompt '{prompt_name}' as artifact.")
#     except Exception as e:
#         logger.error(f"Failed to log prompt '{prompt_name}' as artifact: {e}")

# --- Core Pipeline Function ---
def pipeline(claim: str, llm_instance: ChatOpenAI) -> dict:
    """
    Processes a single claim through the verification pipeline and returns a dictionary
    containing the evidence and confidence score.
    """
    logger.info(f"--- Processing Claim: '{claim}' ---")
    mlflow.log_param("processed_claim_text", claim) # Log the specific claim being processed

    # Step 1: Generate claim dictionary
    logger.info("---Generating claim dictionary---")
    claim_dict = generate_claim_dict(claim, llm_instance, CLAIM_TO_DICTIONARY)
    print("Claim Dictionary:\n",claim_dict)
    logger.debug("Claim Dictionary:\n%s", pp.pformat(claim_dict))
    logger.info("===Claim dictionary generated.===")
    # Log claim_dict as an artifact
    try:
        with open("claim_dictionary.json", "w") as f:
            pp.pprint(claim_dict, stream=f) # Use pprint for structured dict
        mlflow.log_artifact("claim_dictionary.json", artifact_path="results")
        os.remove("claim_dictionary.json")
    except Exception as e:
        logger.error(f"Failed to log claim_dictionary as artifact: {e}")


    # Step 2: Generate keywords
    logger.info("---Generating keywords---")
    keywords = generate_keywords(claim, GENERATE_KEYWORDS, llm_instance)
    print(keywords)
    logger.info("===Keywords Generated.===")
    # Log keywords as an artifact
    try:
        with open("generated_keywords.txt", "w") as f:
            f.write(", ".join(keywords)) # Assuming keywords is a list of strings
        mlflow.log_artifact("generated_keywords.txt", artifact_path="results")
        os.remove("generated_keywords.txt")
    except Exception as e:
        logger.error(f"Failed to log keywords as artifact: {e}")

    # Step 3: Fetch articles
    logger.info("---Fetching Articles---")
    articles = fetch_articles_from_keywords(keywords)
    logger.info("===Articles fetched.===")
    # Log a summary or sample of articles
    try:
        with open("fetched_articles_summary.txt", "w") as f:
            f.write(f"Fetched {len(articles)} articles.\n\n")
            if articles:
                f.write("First 5 articles (titles/URLs):\n")
                for i, article in enumerate(articles[:5]):
                    # Assuming articles are dicts or objects with 'title' and 'url'
                    f.write(f"  - Title: {article.get('title', 'N/A')}\n")
                    f.write(f"    URL: {article.get('url', 'N/A')}\n")
            else:
                f.write("No articles found.\n")
        mlflow.log_artifact("fetched_articles_summary.txt", artifact_path="results")
        os.remove("fetched_articles_summary.txt")
    except Exception as e:
        logger.error(f"Failed to log articles summary as artifact: {e}")


    # Step 4: Generate blank dictionary
    logger.info("---Generating Blank Dictionary---")
    blank_dict = generate_blank_dict(BLANK_DICTIONARY, claim_dict, llm_instance)
    print("Blank Dictionary: \n", blank_dict)
    logger.debug("Blank Dictionary:\n%s", pp.pformat(blank_dict))
    print("===Blank dictionary generated.===")
    # Log blank_dict as an artifact
    try:
        with open("blank_dictionary.json", "w") as f:
            pp.pprint(blank_dict, stream=f)
        mlflow.log_artifact("blank_dictionary.json", artifact_path="results")
        os.remove("blank_dictionary.json")
    except Exception as e:
        logger.error(f"Failed to log blank_dictionary as artifact: {e}")


    # Step 5: Generate article dictionaries
    print("---Generating article dictionaries---")
    article_dictionaries = generate_article_dictionaries(ARTICLE_TO_DICIONARY, blank_dict, articles, llm_instance)
    print("===Article dictionaries generated.===")
    # Log article_dictionaries as an artifact (could be large, consider logging summary)
    try:
        with open("article_dictionaries.json", "w") as f:
            pp.pprint(article_dictionaries, stream=f)
        mlflow.log_artifact("article_dictionaries.json", artifact_path="results")
        os.remove("article_dictionaries.json")
    except Exception as e:
        logger.error(f"Failed to log article_dictionaries as artifact: {e}")

    # Step 6: Generate final dictionary
    logger.info("---Generating Final Dictionary---")
    final_dict = generate_final_dictionary(article_dictionaries, llm_instance, FINAL_DICTIONARY)
    print("Final Dictionary: \n", final_dict)
    logger.debug("Final Dictionary:\n%s", pp.pformat(final_dict))
    logger.info("===Final dictionary generated===")
    # Log final_dict as an artifact
    try:
        with open("final_dictionary.json", "w") as f:
            pp.pprint(final_dict, stream=f)
        mlflow.log_artifact("final_dictionary.json", artifact_path="results")
        os.remove("final_dictionary.json")
    except Exception as e:
        logger.error(f"Failed to log final_dictionary as artifact: {e}")

    # Step 7: Compare claim with evidence
    logger.info("---Comparing claim with evidence---")
    comparison_result = compare_claim_with_evidence(claim_dict, final_dict, llm_instance, CLAIM_VS_EVIDENCE)
    logger.info("===Comparison completed===")
    # Log comparison_result as an artifact and potentially a metric
    try:
        with open("comparison_result.json", "w") as f:
            pp.pprint(comparison_result, stream=f)
        mlflow.log_artifact("comparison_result.json", artifact_path="results")
        os.remove("comparison_result.json")

        # Attempt to log 'confidence' as a metric if it exists in the result
        if isinstance(comparison_result, dict) and "confidence" in comparison_result:
            mlflow.log_metric("confidence_score", comparison_result["confidence"])
            logger.info(f"Logged confidence_score: {comparison_result['confidence']}")

    except Exception as e:
        logger.error(f"Failed to log comparison_result or confidence: {e}")

    return comparison_result

# --- Main function to orchestrate runs ---
def main(user_input: str, llm_instance: ChatOpenAI):
    """
    Takes user input, disintegrates claims, and processes each claim.
    """
    # Log initial user input as a parameter
    mlflow.log_param("initial_user_input", user_input)

    claims = claim_disintegration(user_input, DISSECT_CLAIM, llm_instance)
    all_results = {}

    print("Number of claims found:", len(claims))
    print("Claims found:", claims)
    mlflow.log_param("num_claims_disintegrated", len(claims))
    # Log disintegrated claims
    try:
        with open("disintegrated_claims.txt", "w") as f:
            for claim_item in claims:
                f.write(f"- {claim_item}\n")
        mlflow.log_artifact("disintegrated_claims.txt", artifact_path="results")
        os.remove("disintegrated_claims.txt")
    except Exception as e:
        logger.error(f"Failed to log disintegrated_claims as artifact: {e}")


    if len(claims) == 1:
        # For a single claim, pipeline runs directly within the main run
        result = pipeline(claims[0], llm_instance)
        all_results[claims[0]] = result
    elif len(claims) > 1:
        # If multiple claims, use nested runs for each claim
        for i, claim in enumerate(claims):
            # Start a nested MLflow run for each individual claim
            with mlflow.start_run(nested=True, run_name=f"Claim_Processing_{i+1}"):
                mlflow.log_param("sub_claim_index", i+1)
                mlflow.log_param("sub_claim_text", claim)
                print(f"\n--- Processing Claim {i+1}: '{claim}' ---")
                result = pipeline(claim, llm_instance)
                all_results[claim] = result
    else:
        print("No claims found in the input.")
        mlflow.log_param("no_claims_found", True)

    return all_results

# --- Entry point for the script ---
if __name__ == "__main__":
    # Configure MLflow tracking URI (optional, default is ./mlruns)
    # mlflow.set_tracking_uri("http://localhost:5000") # Uncomment if you have a remote server
    mlflow.set_experiment("Fact_Checker_Pipeline_1") # Set a name for your experiment

    # Start the main MLflow run for the entire execution
    with mlflow.start_run(run_name="Full_Fact_Check_Run_1"):
        # Log LLM parameters
        mlflow.log_param("llm_provider", "OpenAI")
        mlflow.log_param("llm_model_name", llm.model_name)
        mlflow.log_param("llm_temperature", llm.temperature) # Assuming default or configured temperature

        # # Log all prompts as artifacts at the beginning of the main run
        # _log_prompt_as_artifact("CLAIM_TO_DICTIONARY", CLAIM_TO_DICTIONARY)
        # _log_prompt_as_artifact("GENERATE_KEYWORDS", GENERATE_KEYWORDS)
        # _log_prompt_as_artifact("BLANK_DICTIONARY", BLANK_DICTIONARY)
        # _log_prompt_as_artifact("ARTICLE_TO_DICIONARY", ARTICLE_TO_DICIONARY)
        # _log_prompt_as_artifact("FINAL_DICTIONARY", FINAL_DICTIONARY)
        # _log_prompt_as_artifact("CLAIM_VS_EVIDENCE", CLAIM_VS_EVIDENCE)
        # _log_prompt_as_artifact("DISSECT_CLAIM", DISSECT_CLAIM)


        user_input = input("Please provide me with one or more claims to analyze:\n")
        results = main(user_input, llm)
        print("\n--- Overall Results ---")
        for claim, result in results.items():
            print(f"Claim: {claim}")
            print(f"Evidence: {result}")
            print("-" * 20)

        # Log overall results as a final artifact
        try:
            with open("overall_fact_check_results.json", "w") as f:
                pp.pprint(results, stream=f)
            mlflow.log_artifact("overall_fact_check_results.json", artifact_path="final_summary")
            os.remove("overall_fact_check_results.json")
        except Exception as e:
            logger.error(f"Failed to log overall_fact_check_results as artifact: {e}")

    logger.info("MLflow run finished.")