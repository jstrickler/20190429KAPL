#!/usr/bin/env python

target = 'q'

count = 0
with open('DATA/words.txt') as words_in:
    for line in words_in:
        if line.startswith(target):
            count += 1

print(f"{count} words start with {target}")


