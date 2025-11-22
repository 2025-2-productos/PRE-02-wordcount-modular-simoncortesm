### Función read_all_lines

import os


def read_all_lines(input_folder):
    all_lines = []
    input_files_list = os.listdir(input_folder)
    for filename in input_files_list:
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines


### Función preprocess_lines


def preprocess_lines(all_lines):
    all_lines = [line.strip().lower() for line in all_lines]
    return all_lines


### Función count_words


def count_words(words):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter


### Función split_into_words


def split_into_words(all_lines):
    words = []
    for line in all_lines:
        words.extend(words.strip(",.!?") for words in line.split())
    return words


### wordcount.py
# obtain a list of files in the input directory

import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_count_words


def main():

    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        # sys.exit(1)
        return

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = count_words(words)
    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()


### Función write_count_words

import os


def write_count_words(counter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save the results using tsv format
    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")
