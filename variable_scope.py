#!/usr/bin/env python
import sys

x = 1000  # GLOBAL

def spam():
    x = 42
    y = "wombat"  # LOCAL
    print("in spam: x is", x)

spam()

# print("in main: y is",   y)
print("in main: x is", x)

def outer():
    def print(*args, **kwargs):
        sys.stdout.write("HA HA HA\n")

    x = "space the final frontier"

    def inner():
        print("x is", x)
        return "narwhal"

    return inner()  # return VALUE of function
    # return inner  #  return function

f = outer()
print(f)
print("\U0001F92F")
