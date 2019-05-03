#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = sorted(nums)
print("n1: {}\n".format(n1))

s = "spam"
print(s.upper())
print(str.upper(s))

f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def length_and_name(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=length_and_name)
print("f4: {}\n".format(f4))

def wacky(f):
    print("in wacky():", f)
    return f[-1].lower()

f5 = sorted(fruits, key=wacky)
print("f5: {}\n".format(f5))

stuff = ['abc', 15, 28, 3, 'def', 14, 6, 'wombat']

print(sorted(stuff, key=str), '\n')


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

for first_name, last_name, *_ in sorted(people):
    print(first_name, last_name)
print('-' * 60)

def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, product, birth_date in sorted(people, key=by_last_name):
    print(first_name, last_name, product)
print('-' * 60)

n2 = sorted(nums, key=str)
print("n2: {}\n".format(n2))

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print('-' * 60)

def by_value(e):
    return e[1], e[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print('-' * 60)


for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print('-' * 60)


print(sorted(nums, reverse=True, key=str))

fruits.sort(key=str.lower)

print(fruits)

print("\U0001F92F")


