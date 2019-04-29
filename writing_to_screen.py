#!/usr/bin/env python

actor = 'Chris Hemsworth'

value = 22 / 7

print(actor, value)

print(actor, value, sep=" **** ")

print('red', end='*')
print('green', end='&')
print('blue')
print('hello', 'wombat', actor, end='\n\n', sep='X')
print(value)
city = 'Brisbane'

print("{:.3f}".format(value))


print("{} lives in {}".format(actor, city))
print(f"{actor} lives in {city}")
print(f"{2 * city} + {2 * city} is {(2 + 2) * city}")

count = 14

print("Final count is {:04d}".format(count))
print(f"Final count is {count:04d}")

print("Final count is {:4d}".format(count))
print(f"Final count is {count:4d}")



