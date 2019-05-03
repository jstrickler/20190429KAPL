#!/usr/bin/env python
"""
Read flat file with knight data into a dictionary and then display it in various ways.
"""
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'


def main():
    """
    Program entry point

    :return: None
    """
    knight_data = read_data(FILE_NAME)
    pretty_print(knight_data)
    print()
    index_demo(knight_data, 'Galahad')
    print()
    print_title_and_name(knight_data)


def read_data(file_name: str) -> dict:
    """
    Read a colon-separated file into a dictionary where the knight name is the key.

    :param file_name: File to read
    :return: Dictionary of knight data
    """

    data = {}    #   {'Bob': (.....), "Fred": (......)}

    with open(file_name) as knights_in:
        for raw_line in knights_in:
            name, title, color, quest, comment = raw_line.rstrip().split(':')
            data[name] = (title, color, quest, comment)

    return data


def pretty_print(data: str) -> None:
    pprint(data)
    print()


def index_demo(data, knight_name):
    print(data[knight_name])
    print(data[knight_name][0])
    print(data[knight_name][0][0])


def print_title_and_name(data):
    for knight_name, knight_info in data.items():
        print(f"{knight_info[0]} {knight_name}")

if __name__ == '__main__':
    main()
