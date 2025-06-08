import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
import pprint
pp = pprint.PrettyPrinter(indent=4)

from logger import logger # Assuming 'logger' is correctly configured
# api_key = os.environ['OPENAI_API_KEYY']
llm = ChatOpenAI(model='gpt-4o-mini', api_key = os.environ['OPENAI_API_KEYY'])
print(llm.invoke("hi").content)

# Import all your custom modules/functions.
# Assuming these functions internally accept an 'llm_instance' argument.
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

claim = '''Around 150 Blinkit gig workers went on a strike in Varanasi, Uttar Pradesh this weekend demanding fair pay, better working conditions and cotton uniforms for the summer. They now claim that the Zomato-owned grocery delivery platform responded by blocking their IDs – citing the strike as the reason – and made them sign an agreement to have their IDs unblocked.
The recent 90-day tariff truce between the United States and China, which saw the US reducing tariffs on Chinese goods from 145% to 30%, has significant implications for India. 
Virat Kohli retires from test match cricket.'''

claim2 = '''
A US trade court on Wednesday blocked Donald Trump's 'Liberation Day' import tariffs from going into effect, ruling that the President overstepped his authorities with the across-the-board duties on countries that sell more to the United States than they buy. The American Commander in Chief has claimed broad authority to set global tariffs under the International Emergency Economic Powers Act (IEEPA), which is meant to address "unusual and extraordinary" threats during a national emergency. '''
# print(DISSECT_TOPIC)
# topics = dissect_topic(claim, DISSECT_CLAIM, llm=llm)
# for topic in topics:
#     print(topic)

# print([topic for topic in topics])


# for claim in final:
#     print(claim)

# claim_dict = claim_disintegration(claims=final  , prompt = CLAIM_TO_DICTIONARY, llm=gem)
# print(claim_dict)

# print("Claim Dict: ", claim_dict)

# keywords = generate_keywords(claim, GENERATE_KEYWORDS, gem)
# print("KEYWORDS: ",keywords)

# articles = fetch_articles_from_keywords(keywords)
# print("Articles Generated")
# print("sample article:  \n")
# print(articles[0])


# blank_dict = generate_blank_dict(BLANK_DICTIONARY, claim_dict, gem)
# print("Blank dictionary generated: \n")
# print(blank_dict)

# print("Attempting generation of article_to_dict")
# article_dictionaries = generate_article_dictionaries(ARTICLE_TO_DICIONARY, blank_dict, articles, gem)
# print("Articles to dict done")


# final_dict = generate_final_dictionary(article_dictionaries, gem, FINAL_DICTIONARY) 
# print("Final dict generated", final_dict)

# comparison_result = compare_claim_with_evidence(claim_dict, final_dict, gem, CLAIM_VS_EVIDENCE)

# print("Comparison is:")
# print(comparison_result)





