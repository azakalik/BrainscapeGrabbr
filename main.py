from check_valid_brainscape_url import check_valid_brainscape_url
from loguru import logger
from scrape_flashcards import scrape_flashcards
from write_flashcards_to_file import write_flashcards_to_file


def main(brainscape_url: str) -> None:
    study_set, pack_id = check_valid_brainscape_url(brainscape_url)

    logger.info(f'Scraping pack: {pack_id} from study set {study_set}')
    flashcards = scrape_flashcards(brainscape_url)
    logger.info(f'Finished scraping flashcards')

    write_flashcards_to_file(flashcards)
    logger.info(f'Finished writing flashcards to file')


if __name__ == '__main__':
    main('https://www.brainscape.com/flashcards/pod-13735762/packs/21442051')
