#!/usr/bin/env python
import sys

if len(sys.argv) >= 2:
    limit = int(sys.argv[1])
else:
    limit = 100

limit += 1  # allow for 0-based indexing

flags = [True] * limit

for num in range(2, limit):
    if flags[num]:
        print(num, end=', ')  # num is prime
        for j in range(num, limit, num):
            flags[j] = False


