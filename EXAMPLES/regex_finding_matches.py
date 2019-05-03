#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

pattern = r'[A-Z]\d{2,3}'  # <1>

if re.search(pattern, s):  # <2>
    print("Found pattern.")
print()

m = re.search(pattern, s)  # <3>
print(m)
if m:
    print("Found:", m.group(), m.start(), m.end(), m.span())  # <4>
print()

# re.match(^...) # match beg. of string or line re.fullmatch(^...$)  # match string or line

#  x = "28938"
#  re.fullmatch(r'\d+', x)
#  re.search(r'^\d+$', x)

#  "DL2344"   "N1234"
#  re.fullmatch(r'


for m in re.finditer(pattern, s):  # <5>
    print(m.group(), m.start())
print()

matches = re.findall(pattern, s)  # <6>
print("matches:", matches)
