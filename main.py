import csv

# Example card data
cards = [
    {
        'Word (Kana)': 'たべる',
        'Word (Kanji)': '食べる',
        'English Definition': 'to eat',
        'Japanese Definition': '食事をする',
        'Example Usage': 'ごはんをたべる',
    },
    {
        'Word (Kana)': 'ねる',
        'Word (Kanji)': '寝る',
        'English Definition': 'to sleep',
        'Japanese Definition': '睡眠をとる',
        'Example Usage': 'ねむいのでねる',
    },
    {
        'Word (Kana)': 'のむ',
        'Word (Kanji)': '飲む',
        'English Definition': 'to drink',
        'Japanese Definition': '液体をとる',
        'Example Usage': 'おちゃをのむ',
    },
]

# Specify the output CSV file path
output_file = 'example_cards.csv'

# Write the card data to the CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Word (Kana)', 'Word (Kanji)', 'English Definition', 'Japanese Definition', 'Example Usage'])
    writer.writeheader()
    writer.writerows(cards)

print(f"Example cards written to {output_file}.")