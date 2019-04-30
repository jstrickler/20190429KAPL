#!/usr/bin/env python
# from MODULE import NAME
from pprint import pprint
import sys

list1 = list()  # empty list
list2 = ['a', 'b', 'c', 2, 3, None]
list3 = []

cities = ['Poughkeepsie', 'Saratoga Springs',
    'Albany', 'Colonie', 'Rensselaer']

print(cities[0], cities[4])
print(cities[-1])
print(cities[len(cities)-1])
print(len(cities))
print(cities[-2], cities[-4])

foo = [[['moar', 'moar', 'moar'],1,2,3], [4, ['naught', 'programmer'], 6], [7, 8, 9]]

print(foo[0][0])
print(foo[-1][-1])
# print(foo[-1, -1])


pprint(foo)
print()
print(foo)
pprint(list2)
print('\U0001F92F')

print(cities)
cities.append('Schenectady')
print(cities)
cities.insert(0, "Malta")
print(cities)

cities.insert(4, "Schuylerville")
print(cities)

more_cities = ['Manhattan', 'Troy', 'Ithaca']

cities.extend(more_cities)

print(cities)

del cities[-2]
print(cities)

cities.remove('Manhattan')

print(cities, '\n')

c = cities.pop()
print(c)
print(cities)
print()

c = cities.pop(3)
print(c)
print(cities)
print()



print(cities.index('Schuylerville'))

food = ['spam', 'spam', 'spam', 'eggs', 'bacon','spam']

print(food.index('spam'))
print(food.index('spam', 3))

# TARGET = 'spam'
# pos = -1
# while TARGET in food:
#     pos = food.index(TARGET, pos + 1)
#     print(pos)
#     if TARGET not in food:
#         break

print('\U0001F92F')

cities.append('Buffalo')
cities.append('Amsterdam')
cities.append('Queensbury')
cities.append('Ticonderoga')
cities.append('Watkins Glen')

print(cities)

print(cities[0], cities[9], cities[-1], '\n')

print(cities[0:4])
print(cities[5:9])

s = 'mugwump'
print(s[0:-1])

#   SEQ[START:STOP]   SEQ[START:STOP:STEP]
#   SEQ[:STOP]  SEQ[START:] SEQ[::]
#   SEq[::STEP]
print(cities[:4])
print(cities[-3:])

actor = 'Chris Hemsworth'

print(actor[:5])
print(actor[-5:])
print(actor[6:9])

# cities.append(['A', 'B', 'C'])

print(cities)

# for VAR ... in ITERABLE:
for city in cities:
    #  city = next(cities)
    #  do block
    #  lather, rinse, repeat....
    print(city)
print('-' * 60)

for city in cities[1:]:
    print(city)
print('-' * 60)

for p in sys.argv[1:]:
    print(p)

print(actor, '\n')
for c in actor:
    print(c, end=' ')
print()
print("\U0001F92F")





