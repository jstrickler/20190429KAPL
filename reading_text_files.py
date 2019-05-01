#!/usr/bin/env python

#  file_object = open(file_path, "mode")
#  mode is r, w, a, or x  (or rb, wb, ab, or xb)

#  mary_in = open('DATA/mary.txt')

# with EXPR as VAR:
# with EXPR:

# read line by line
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in: # including \n
        line = raw_line.rstrip('\n\r')
        print(line)

print('-' * 60)

# read entire file
with open('DATA/mary.txt') as mary_in:
    contents =  mary_in.read()
    print(contents)
    print('=' * 20)
    print(repr(contents))

print('-' * 60)

# read into list WITH newlines
with open('DATA/mary.txt') as mary_in:
    lines = mary_in.readlines()
    print(lines)
print('-' * 60)

# read into list WITHOUT newlines
with open('DATA/mary.txt') as mary_in:
    lines = [line.rstrip() for line in mary_in]
    print(lines)
print('-' * 60)

# create generator WITHOUT newlines (generator rather than list)
with open('DATA/mary.txt') as mary_in:
    lines = (line.rstrip() for line in mary_in)

    print(lines)
    print("A:")
    for line in lines:
        print(line)

print('-' * 60)
