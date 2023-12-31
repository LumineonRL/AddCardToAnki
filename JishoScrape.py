import requests
import re
from bs4 import BeautifulSoup
from typing import Tuple, List, Optional


class JishoScrape:
    def __init__(self, word: str) -> Tuple[Optional[List[str]], Optional[List[str]], Optional[List[str]]]:
        self.word = word
        self.url = f'https://jisho.org/word/{word}'
    
    def save_raw_html(self):
        response = requests.get(self.url)
        with open('rawpage5.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
            
    def filter_kanji(self, strings: List[str]) -> List[str]:
        kanji_pattern = re.compile(r'[\u4e00-\u9faf]')
        filtered_strings = [s for s in strings if not kanji_pattern.search(s)]
        return filtered_strings

    def scrape_word_info(self) -> None:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        readings = self._scrape_readings(soup)
        readings = self.filter_kanji(readings)
        
        definitions = self._scrape_definitions(soup)
        
        examples = self._scrape_examples(soup)
        
        return readings, definitions, examples
    
    def _scrape_readings(self, soup: BeautifulSoup) -> List[str]:
        readings = []
        reading_elements = soup.select('.concept_light-status a[href*="/search/"]')
        for element in reading_elements:
            reading_text = element.text.strip()
            if 'Sentence search' in reading_text:
                reading_text = reading_text.replace('Sentence search for ', '')
                readings.append(reading_text)
        return readings
    
    def _scrape_definitions(self, soup: BeautifulSoup) -> List[str]:
        definitions = []
        definition_elements = soup.select('.meanings-wrapper .meaning-meaning')
        for element in definition_elements:
            definitions.append(element.text.strip())
        return definitions
    
    def _scrape_examples(self, soup: BeautifulSoup) -> List[str]:
        examples = []
        example_elements = soup.select('.sentence > .clearfix.japanese_gothic.japanese')
        for element in example_elements:
            example_text = element.text.strip()
            example_text = re.sub(r'[\n\s]+', ' ', example_text)  # Remove extra spaces and newlines
            examples.append(example_text)
        return examples