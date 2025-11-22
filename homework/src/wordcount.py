# obtain a list of files in the input directory
import os

from ._internals.write_count_words import write_count_words


def main():
    ## read all lines
    all_lines = []
    input_files_list = os.listdir("data/input/")
    for filename in input_files_list:
        file_path = os.path.join("data/input", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    ### preprocess lines
    all_lines = [line.strip().lower() for line in all_lines]

    ### split in words
    words = []
    for line in all_lines:
        words.extend(words.strip(",.!?") for words in line.split())

    ### count words
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_files_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    write_count_words(counter)


if __name__ == "__main__":
    main()


# create the directory output/ if it doesn't exist
# def write_count_words():
#     if not os.path.exists("data/output"):
#         os.makedirs("data/output")

#     # save the results using tsv format
#     with open("data/output/results.tsv", "w", encoding="utf-8") as f:
#         for key, value in counter.items():
#             # write the key and value to the file
#             f.write(f"{key}\t{value}\n")
