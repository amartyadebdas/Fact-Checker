import os
import requests
from dotenv import load_dotenv
from typing import List, Dict
# from data.keywords.keywords_for_api import keywords_claim

def fetch_articles_from_keywords(
    keywords: str,
    number: int = 10,
    language: str = "en"
) -> List[Dict]:
    """
    Fetches news articles using keywords from the World News API.

    Args:
        keywords (str): The keyword string to search for.
        number (int): Number of articles to retrieve.
        language (str): Language of articles.

    Returns:
        List[Dict]: A list of news article objects.
    """
    load_dotenv()
    api_key = os.environ.get("WORLDNEWS_API_KEY_CHOWDHURY")

    if not api_key:
        raise ValueError("WORLDNEWS_API_KEY_CHOWDHURY is not set in environment variables.")

    base_url = "https://api.worldnewsapi.com/search-news"

    params = {
        "api-key": api_key,
        "text": keywords,
        "language": language,
        "number": number
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        articles = data.get("news", [])
        return [article.get("text", "") for article in articles if article.get("text")]

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
        return []