from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("word")

args = parser.parse_args()

chosen_word = args.word

path = Path('Field Artillery Training. 1914 by GB War Office.txt')

try:
    contents = path.read_text()
except FileNotFoundError:
    print("No such file exists")
else:
    words = contents.split()
    occurrences = words.count(chosen_word)
    print(f"The word '{chosen_word}' appears {occurrences} times in the given file.\n")