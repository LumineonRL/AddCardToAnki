# AddCardToAnki

Adds a list of Japanese words in a comma separated .txt file to a .csv file that can them be imported to Anki.
Resultant csv will contain info on the word's reading, english definition, japanese definition, and example sentences (if available).

This program assumes you have the `wnjpn.db` sqlite file obtained from https://bond-lab.github.io/wnja/index.en.html . It is too large to upload to this repository. It should be located in a folder called `JapaneseWordNet` in the root.

To run: run `main.py`. Currently expects your .txt file to be named `wordstoadd.txt` located in the root. Adding that as a CLI is on my to do list.

Resultant .csv will be called `cards_to_add.csv` and located in the root. This is meant to be imported into anki Desktop. There is currently no support for custom fields outside of the ones provided.
