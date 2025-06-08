import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from prompts.topic_dissection import DISSECT_TOPIC
from langchain.prompts import ChatPromptTemplate
load_dotenv()


# llm = ChatOpenAI(model='gpt-4o-mini', api_key = api_key)

def dissect_topic(claim:str, prompt:str, llm:ChatOpenAI):
    
    final_prompt = ChatPromptTemplate.from_messages([
        ('system',prompt),
        ('human','{input}')
    ])
    
    chain = final_prompt | llm
    response = chain.invoke({
        "input":claim
    })
    response = response.content.split("\n")

    response = [topic for topic in response if len(topic)!=0]
    
    return response
