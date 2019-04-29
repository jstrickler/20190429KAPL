#!/usr/bin/env python
import re

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the founder")
print('Guido is the "BDFL" of Python')

print("""Guido's the "BDFL" of Python""")

insert_rows = """
    insert into wombats
    (name, habitat)
    values (?, ?)
"""

s5 = r"spam\n"   #
jing = "spam\\n\n"
print(jing)

actor = "Chris Hemsworth"

a1 = actor.upper()
print(actor, a1)

print(actor.count('h'))
print(actor.count('wort'))
print(actor.count('H'))
print(actor.lower())
print(actor.lower().count('h'))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("wort" in actor)
print("hops" in actor)

data = "foo:bar:baz::blech"

fields = data.split(':')
print(fields)

words = "wombat       lemur         coatimundi".split()
print(words)

stuff = "foo, bar, blah, baz"
print(stuff.split(', '))

jing2 = r"\junk\more\stuff\Jing-Fang"

fields = re.split(r'[\\-]', jing2)
print(fields)
print(fields[1])
print(actor.index('wor'))
print(actor.index('is'))
print(actor.index('r'))
print(actor.rindex('r'))

#             1
#   01234567890123456
#   Chris Hemsworth


s = "            My hovercraft is full of eels                "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "hoverhoverhoverMy hovercraft is full of eelshoverhoverhover"
print("|" + s.lstrip("rhove") + "|")
print("|" + s.rstrip("hvoer") + "|")
print("|" + s.strip("rehov") + "|")
print()

x = "   ;    wombat.   "

new_x = x.strip(' ,;.')

# $x =~ s/(^[ ,;.])|([ ,;.]$)//g;

print(">{}<".format(new_x))

#


s = "It's a right night nice for ice cream"

print(s.index("ight"))
print(s.index("ight", 10))
print(s.index("ight", 10, 16))










