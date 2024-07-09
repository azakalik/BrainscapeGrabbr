import re


def check_valid_brainscape_url(brainscape_url: str) -> tuple[str, str]:
    pattern = r"https://www\.brainscape\.com/flashcards/([^/]+)/packs/([^/]+)"
    match = re.match(pattern, brainscape_url)
    if match:
        return match.groups()
    else:
        raise ValueError("Brainscape URL is not valid")
