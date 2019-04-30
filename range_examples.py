#!/usr/bin/env python

for i in range(10):
    print("Do not pet the wombat!")
print()

for i in range(1, 11):
    print(i, end='' if i == 10 else ', ')
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print()

for i in range(2, 101, 2):
    print(i, end=' ')
