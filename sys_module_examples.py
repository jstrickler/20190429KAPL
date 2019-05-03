#!/usr/bin/env python
import sys
import re
from pprint import pprint

print(sys.version_info)
print(sys.platform)
print()
print(sys.prefix)
print(sys.executable)
print()
for path in sys.path:
    print(path)
print()

print(sys.modules['re'])
print(sys.modules['re'].findall('[a-z]+', 'foo bar blah'))
print(re.findall('[a-z]+', 'foo bar blah'))
print(sys.modules.keys())
print()

print(dir(sys))
print()
print(sys.maxsize, '\n')
pprint(sys.modules)
print()

x = 5
print(dir(x))
print(x + 5)
print(x.__add__(5))


s = "foo"
print(dir(s))


