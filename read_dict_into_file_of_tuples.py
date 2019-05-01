#!/usr/bin/env python
from pprint import pprint

knight_data = {}    #   {'Bob': (.....), "Fred": (......)}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_data[name] = (title, color, quest, comment)

pprint(knight_data)
print()
print(knight_data['Galahad'])
print(knight_data['Galahad'][0])
print(knight_data['Galahad'][0][0])

#     KEY         VALUE   in   DICT.items()
#    str,        tuple    in ....
for knight_name, knight_info in knight_data.items():
    print(f"{knight_info[0]} {knight_name}")
print('-' * 60)

#      key, (value1, ...)
for knight_name, (k_title, k_color, k_quest, k_comment) in knight_data.items():
    print(f"{k_title} {knight_name}")

