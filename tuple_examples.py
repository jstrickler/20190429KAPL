#!/usr/bin/env python

t = tuple()

# person = ('Bill', 'Gates', 'Microsoft')

person = ('Bill', 'Gates', 'Microsoft')

print(person)

print(person[0], person[1])

print(len(person))

# iterable unpacking
# list of variables = any_iterable
first_name, last_name, product = person

values = ['a', 'b', 'c', 'd', 'e', 'f']

# extended unpacking
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft Foundation', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'git', 'Linux', '1969-12-28'),
    ('John', 'Strickler',  '1950-1-1'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for first_name, last_name, *_, birth_date in people:
    print(f"{first_name:15s} {last_name:15s} {birth_date}")
print()









