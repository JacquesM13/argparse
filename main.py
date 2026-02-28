from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("word")
parser.add_argument("path")

args = parser.parse_args()

chosen_word = args.word
file_path = args.path

path = Path(file_path)

try:
    contents = path.read_text()
except FileNotFoundError:
    print("No such file exists")
else:
    words = contents.split()
    occurrences = words.count(chosen_word)
    print(f"The word '{chosen_word}' appears {occurrences} times in the given file.\n")