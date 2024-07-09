import re


class Flashcard:
    def __init__(self, question: str, answer: str):
        self.question = clean_text(question)
        self.answer = clean_text(answer)


def clean_text(text: str):
    # Remove any appearance of '\nA\n' and '\nQ\n'
    text = text.replace('\nA\n', '').replace('\nQ\n', '')

    # Replace multiple consecutive newlines with a single newline
    text = re.sub(r'\n+', '\n', text)

    return text
