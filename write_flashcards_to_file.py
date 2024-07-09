from typing import List
from flashcard import Flashcard


def write_flashcards_to_file(flashcards: List[Flashcard], filename: str = 'flashcards.txt'):
    with open(filename, 'w') as file:
        for flashcard in flashcards:
            file.write(f"Question: {flashcard.question}\n")
            file.write(f"Answer: {flashcard.answer}\n\n")
