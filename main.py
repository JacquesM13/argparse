from pathlib import Path
import argparse
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='runtime.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S')

parser = argparse.ArgumentParser()

parser.add_argument("word")
parser.add_argument("path")

args = parser.parse_args()

chosen_word = args.word
file_path = args.path

path = Path(file_path)

def word_count(doc, word):
    return doc.count(word)

try:
    contents = path.read_text()
except FileNotFoundError:
    print("No such file exists")
    logger.error("Attempted run with file not found, %s", file_path)
else:
    words = contents.split()
    occurrences = word_count(words, chosen_word)
    print(f"The word '{chosen_word}' appears {occurrences} times in the {file_path}.\n")