import xml.etree.ElementTree as ET
from typing import Tuple, List, Optional

# Relative path to the JMdict_e_example.xml file
xml_file = 'JMDict/JMdict_e_examp.xml'

def extract_word_info(xml_file: str, word: str) -> Tuple[Optional[List[str]], Optional[List[str]], Optional[List[str]]]:
    # Register the 'xml' namespace prefix
    ET.register_namespace('', 'http://www.w3.org/XML/1998/namespace')

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    readings = []
    definitions = []
    examples = []

    # Find the entry for the word
    for entry in root.findall('.//entry'):
        for k_ele in entry.findall('.//k_ele'):
            # Check if the word matches the input
            if k_ele.find('keb').text == word:
                # Extract the readings
                for r_ele in entry.findall('.//r_ele'):
                    reading_element = r_ele.find('reb')
                    if reading_element is not None:
                        readings.append(reading_element.text)

                # Extract the English definitions
                definitions = [gloss.text for gloss in entry.findall('.//gloss')]

                # Extract the examples
                for example in entry.findall('.//example'):
                    example_text = example.find('.//ex_sent[@xml:lang="jpn"]', namespaces={'xml': 'http://www.w3.org/XML/1998/namespace'})
                    if example_text is not None:
                        examples.append(example_text.text)

                # Return the extracted information
                return readings, definitions, examples
    
    # If the word is not found, return None for all the information
    return None, None, None