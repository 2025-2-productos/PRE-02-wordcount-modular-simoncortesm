import os


def write_count_words(counter):
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")
