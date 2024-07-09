import requests
from bs4 import BeautifulSoup
from loguru import logger
from flashcard import Flashcard
from typing import List


def scrape_flashcards(brainscape_url: str) -> List[Flashcard]:
    response = requests.get(brainscape_url)
    if response.status_code != 200:
        logger.error(f"Failed to retrieve page with status code: {response.status_code}")
        raise Exception(f"Failed to retrieve page with status code: {response.status_code}")

    scraped_flashcards = []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find visible flashcards
    flashcards_html = soup.select('.flashcards-list-layout .flashcard-row')
    for card in flashcards_html:
        question = card.select('.flashcard-contents.question-contents')[0].text
        answer = card.select('.flashcard-contents.answer-contents.back')[0].text
        scraped_flashcards.append(Flashcard(question, answer))

    return scraped_flashcards
