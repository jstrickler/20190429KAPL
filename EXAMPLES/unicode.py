#!/usr/bin/env python

print('26\u00B0')  # <1>
print('26\N{DEGREE SIGN}')  # <2>
print(r'26\u00B0\n')  # <3>
print()

print('we spent \u20ac1.23M for an original C\u00e9zanne') # <4>
print("Romance in F\u266F Major")
print()

data = ['\U0001F95A', '\U0001F414', '\N{CHICKEN}', '\N{EGG}'] # <5>
print(sorted(data))

#  \n \r
#  UNIX/MAC  \x0A
#  WINDOWS   \x0A\x0D

spam = "abc\
    def"

print(spam)

print("\a\a\a")

