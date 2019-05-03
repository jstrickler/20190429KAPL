#!/usr/bin/env python
import sys

#     pkg.pkg           module
from kapl.misc import kapllib

# search algorithm
# 1. current folder
# 2. folders in PYTHONPATH environment variable
# 3. installation folders for your version of Python

kapllib.spam()
kapllib.ham()
kapllib._eggs()



kapllib.main()

print(kapllib.CITIES)

print('-' * 60)
for path in sys.path:
    print(path)
