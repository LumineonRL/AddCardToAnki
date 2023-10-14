import sqlite3
from typing import List

def extract_japanese_definitions(word: str) -> List[str]:
    conn = sqlite3.connect('JapaneseWordNet/wnjpn.db')
    cursor = conn.cursor()

    # Execute the SQL query to extra the Japanese definition(s) for the provided word
    query = f'''
    WITH word_id AS (
        SELECT wordid
        FROM word
        WHERE lemma = '{word}'
    ),
    sense_synset AS (
        SELECT synset
        FROM sense
        WHERE wordid IN (SELECT wordid FROM word_id)
            AND lang = 'jpn'
    ),
    definition AS (
        SELECT def
        FROM synset_def
        WHERE synset IN (SELECT synset FROM sense_synset)
            AND lang = 'jpn'
    )
    SELECT def
    FROM definition;
    '''

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # Extract the definitions from the query results
    definitions = [result[0] for result in results]

    return definitions