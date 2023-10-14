import csv
from tqdm import tqdm
from ParseJMDict import extract_word_info
from ParseJapaneseWordNet import extract_japanese_definitions
from JishoScrape import JishoScrape
from typing import Tuple, List, Dict, Union

def read_words_from_file(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split(',')
        return [word.strip() for word in words]

def create_card(word: str, readings: Union[str, List[str]], definitions: Union[str, List[str]], 
                japanese_definitions: Union[str, List[str]], examples: Union[str, List[str]]) -> Dict[str, str]:
    def join_if_list_or_tuple(value: Union[str, List[str]]) -> str:
        if isinstance(value, (list, tuple)):
            return ', '.join(value)
        return value

    card = {
        'Word (Kana)': join_if_list_or_tuple(readings),
        'Word (Kanji)': word,
        'English Definition': join_if_list_or_tuple(definitions),
        'Japanese Definition': join_if_list_or_tuple(japanese_definitions),
        'Example Usage': join_if_list_or_tuple(examples),
    }

    return card

def extract_word_info_with_scraping(xml_file: str, word: str) -> Tuple[List[str], List[str], List[str]]:
    # Extract word information from JMDict
    readings, definitions, examples = extract_word_info(xml_file, word)
    
    if not definitions:
        # If definitions are empty, scrape word information from Jisho.org
        jisho_scrape = JishoScrape(word)
        readings, definitions, examples = jisho_scrape.scrape_word_info()
        
        return readings, definitions, examples
    
    return readings, definitions, examples

def main():
    # Relative path to the JMdict_e_example.xml file
    xml_file = 'JMDict/JMdict_e_examp.xml'

    # Read the list of words from the input file
    input_file = 'wordstoadd.txt'
    words = read_words_from_file(input_file)

    # Initialize an empty list to store the cards
    cards = []

    # Loop through each word in the words list
    for word in tqdm(words):
        # Extract word information
        readings, definitions, examples = extract_word_info_with_scraping(xml_file, word)
        japanese_definitions = extract_japanese_definitions(word)

        # Create a dictionary for each word
        card = create_card(word, readings, definitions, japanese_definitions, examples)

        # Add the card to the cards list
        cards.append(card)

    # Specify the output CSV file path
    output_file = 'cards_to_add.csv'

    # Write the card data to the CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Word (Kana)', 'Word (Kanji)', 'English Definition', 'Japanese Definition', 'Example Usage'])
        writer.writerows(cards)

    print(f"Cards written to {output_file}.")

if __name__ == '__main__':
    main()