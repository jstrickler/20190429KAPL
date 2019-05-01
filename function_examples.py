#!/usr/bin/env python

def get_message():  # define parameters
    return "Hello, KAPL world"

m = get_message()  # call with arguments
print(m, '\n')

def say_hello():
    m = get_message()
    print(m)

say_hello()


print()


def hello(whom:str='world') -> None:
    print(f"Hello, {whom}")


hello("Mom")
hello("world")
print("Using default value:")
hello()

greetee = 'Mr. Wombat'

hello(greetee)
hello(1.234)

def make_legend(title, colors):
    print("colors as object:", colors)


make_legend("rainfall", ['red', 'blue', 'green'])

def make_legend2(title, *colors):
    print("colors:", colors)


make_legend2("rainfall", 'red', 'blue', 'green')
make_legend2("goat curry")

def spam(a, b, c, *d):
    print(a, b, c, d)

spam('x', 'y', 'z', 1.5, None, "wombat", 'm')


def whatever(p1, p2, *p3, foo, bar, **p4):
    print("whatever: p4:", p4)

def something(p1, p2, *, foo, bar, **p3):
    pass


whatever(5, 6, foo=7, bar=8, spam=12, ham="weasel")


# def open(file_name, mode='r'):
#     pass




