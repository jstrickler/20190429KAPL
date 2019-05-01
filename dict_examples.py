#!/usr/bin/env python
from pprint import pprint

d1 = dict()
d2 = {'a': 5, 'b': 10, 'd': 18, 'r': 3}
print(len(d2))
d3 = {}

stcaps = {
    'NY': 'Albany',
    'MA': 'Boston',
    'VT': 'Montpelier',
    'NH': 'Concord',
    'PA': 'Harrisburg',
}

pprint(stcaps)
print()
print(stcaps['NH'])
print(stcaps.get('NC'))
print(stcaps.get('NC', 'Not found'))
print(stcaps.setdefault('NC', 'Raleigh'))
pprint(stcaps)
stcaps.setdefault('FL')
pprint(stcaps)

print(stcaps.keys())
print(stcaps.values())

print(stcaps['NY'])


for state, capital in stcaps.items():
    print(state, capital)
print()

# NOT PYTHONIC:
# for state in stcaps:  # BAD PROGRAMMER! NO BISCUITS!
#     print(state, stcaps[state])
print(stcaps.items(), '\n')

for x in stcaps:
    print(x)
print()


for v in stcaps.values():
    print(v)
print()

more_capitals = {'NY': 'Corning', 'DE': 'Dover', "NJ": "Trenton",
                 "NY": 'Albany'}


stcaps.update(more_capitals)
pprint(stcaps)
print()

for state in 'NY', 'NC', 'NJ', 'WY', 'AZ', 'NM', 'MA':
    print(state, state in stcaps)
print()

stcaps['ME'] = "Augusta"

pprint(stcaps)
print()

stcaps['ME'] = 'Wombat City'
stcaps['NY','FL'] = 'Albany', 'Tallahassee'

pprint(stcaps)
print()

