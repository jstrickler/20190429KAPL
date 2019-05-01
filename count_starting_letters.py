#!/usr/bin/env python
from pprint import pprint
from collections import Counter

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]
        if first_letter not in letter_counts:
            letter_counts[first_letter] = 0

        letter_counts[first_letter] += 1  # add to count

pprint(letter_counts)
print('-' * 60)

c = Counter(['a', 'b', 'a', 'b', 'c'])
print(c)


letter_counts = Counter()

with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]
        letter_counts[first_letter] += 1
    print(letter_counts)
print("=" * 60)
with open('DATA/words.txt') as words_in:
    letter_counts = Counter(line[0] for line in words_in)
    print(letter_counts)
