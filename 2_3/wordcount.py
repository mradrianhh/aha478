import sys
import sys

words: dict = {}

with open(sys.argv[1], "r") as file:
    all_words = []
    for line in file:
        for word in line.replace(".", "").replace(",", "").replace("\n", "").replace("\t", "").split(" "):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

for word in words:
    print(f"{word}: {words[word]}")