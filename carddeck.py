#!/usr/bin/env python
import random

class CardDeck:

    _SUITS = 'clubs diamonds hearts spades'.split()
    _RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()


    def _make_deck(self):
        self._cards = []
        for suit in self._SUITS:
            for rank in self._RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property (AKA accessor)
        return self._dealer
    # dealer = property(dealer)

    @dealer.setter
    def dealer(self, dealer):  # setter prop (AKA mutator)
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    #  prop    getter only
    #  props   getter + setter

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        t = type(self)
        class_name = t.__name__
        return "{}({})".format(class_name, len(self))
