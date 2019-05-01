#!/usr/bin/env python

limit = 10000001

non_prime = set()
count = 0
for num in range(2, limit):
    if num not in non_prime:
        count += 1
        # print(num, end=", ")
        for i in range(num, limit, num):
            non_prime.add(i)
print()

print(f"There are {count} primes less than {limit}")
