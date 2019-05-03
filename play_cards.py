#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

# d1 is an INSTANCE of the CardDeck CLASS
d1 = CardDeck('Clare')   #  CardDeck d1 = new CardDeck();

print(d1.dealer)

d1.dealer = "Fred"

print(d1.dealer)

try:
    d1.dealer = 2334
except TypeError as err:
    print(err)


print(d1.dealer)

d1.shuffle()

print(d1.cards, '\n')

for i in range(8):
    print(d1.draw())
print()

print(len(d1))

print(d1)

j1 = JokerDeck("Jill")
print(j1)
j1.shuffle()
print(j1.draw())
print(j1.cards)
j1.beep()

