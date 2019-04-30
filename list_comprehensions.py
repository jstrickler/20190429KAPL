#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "Pear", "banana", "tamarind", "persimmon",
"elderberry", "Peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

# RESULT = [THING_TO_APPEND for VAR ... in ITERABLE if COND]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

# my @x = u($y) for my $y in @stuff;

f3 = [f for f in fruits if f.lower().startswith('p')]
print("f3: {}\n".format(f3))

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [(r,s) for r in ranks for s in suits]

print(cards, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

full_names = [f"{p[0]} {p[1]}" for p in people]
print(full_names, '\n')

data = [list(p[:2]) for p in people]
print(data, '\n')

stuff = [(i, i ** 2, i ** 3, round(i ** .5, 2)) for i in range(10)]
print(stuff, '\n')

a = ['blue', 'green', 'red']
b = ['big', 'little', 'huge']
c = ['wombat', 'hippo', 'elephant']

things = [(x, y, z) for x in a for y in b for z in c]

print(things, '\n')

f5 = [(f, len(f), f.upper()) for f in fruits if f.startswith('p') if len(f) > 8]

print("f5: {}\n".format(f5))

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'eggs',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'toast']

food2 = [f for f in food if f != 'spam']
print(food2)

g1 = (f.upper() for f in fruits)
# print("g1: {}\n".format(g1))
for fruit in g1:
    print(fruit)







