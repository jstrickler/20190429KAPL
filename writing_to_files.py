#!/usr/bin/env python

mode = 'w'

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitdata.txt', mode) as fruitdata_out:
    for fruit in sorted(fruits):
        fruitdata_out.write(fruit + '\n')


with open('DATA/mary.txt') as mary_in:
    with open('umary.txt', 'w') as mary_out:
        for line in mary_in:
                mary_out.write(line.upper())
