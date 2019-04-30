#!/usr/bin/env python

fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']
name = "Eric Idle"
knight = 'King', 'Arthur', 'Britain'
stuff = b'abc\x99'

print(fruits[3])  # <1>
print(name[0])  # <2>
print(knight[1])  # <3>
print(stuff[3])
print(stuff[0])
print([int(x) for x in stuff])

