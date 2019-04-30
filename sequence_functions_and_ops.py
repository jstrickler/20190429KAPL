#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(min(nums), max(nums), sum(nums), len(nums))

actor = 'Chris Hemsworth'

print(min(actor), max(actor), len(actor))

print(sorted(nums))
print(sorted(actor))

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

print(sorted(fruits))

x = ['a', 'b', 'c', 'd', 'e', 'f']

for c in reversed(x):
    print(c)

print(reversed(x))

# for INDEX_VAR, VALUE_VAR  in enumerate(ANY_ITERABLE):
for i, item in enumerate(x, 1):
    print(i, item)

print(list(enumerate(x)))

foo = ['a', 'b', 'c']
bar = ['d', 'e', 'f']

blah = foo + bar

baz = [foo * 5, bar * 3] * 20
print(baz)

print(blah)

flags = [True] * 20

line = '-' * 60

print(flags)
print(line)

print(True * 20)


print(line)

print([0] * 10)
print("WOMBAT! " * 50)
