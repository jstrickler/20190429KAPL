#!/usr/bin/env python
john_countries = """Canada
Canada
Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split()

clare_countries = """Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split()

print(john_countries)
print(clare_countries)
print()

john = set(john_countries)
clare = set(clare_countries)
print()

print(john)
print(clare)
print()

print("both:", john & clare)
print("just one:", john ^ clare)
print("all:", john | clare)
print("just Clare:", clare - john)
print("just John:", john - clare)


s = set(['x', 'y', 'z'])

stuff = ['a', 'b', 'c']

s.update(stuff)

junk = range(5)

s.update(junk)

print(s)





