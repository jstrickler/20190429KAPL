#!/usr/bin/env python
import sys

# def print(*args, **kwargs):
#     sys.stdout.write("Hi Mom!\n")
#     for i, item in enumerate(args):
#         sys.stdout.write(str(item) +  (' ' if i < (len(args)-1) else '\n'))

print(sys.stdin, sys.stdout, sys.stderr)

print("Your hair's on fire!", file=sys.stderr)

