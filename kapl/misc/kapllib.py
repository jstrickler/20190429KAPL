#!/usr/bin/env python
# import blunderfuss
"""
Library of awesome code for Knolls Atomic Power Labs
"""

CITIES = ["Albany", 'Latham', 'Colonie']

class Clown():
    """
    A scary circus performer.
    """
    pass

class Room():
    """
    Part of a building.
    """
    pass

def main():
    print("Hello KAPL")
    spam()
    ham()

def spam():
    """
    Fatty pork meat.

    :return: None
    """
    print("Hello from spam()")

def ham():
    """
    Delicious leg of pig.

    :return: None
    """
    print("Hello from ham()")

def _eggs():
    'Hen fruit'
    print("Hello from _eggs()")


def doit(file_name, city):
    """
    Do something important

    :param file_name: file to process
    :param city: only pull records from this city
    :return: average number of cats owned as integer
    """
    pass

#  reStructuredText
# sphinx

if __name__ == '__main__': # if running as script (not imported as module)
    main()

