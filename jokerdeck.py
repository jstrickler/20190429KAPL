#!/usr/bin/env python

from carddeck import CardDeck

class Beeper:
    def beep(self):
        print("Beep! Beep!")


class JokerDeck(Beeper, CardDeck):

    def _make_deck(self):
        super()._make_deck()
        jokers = [
            ('Joker', 1),
            ('Joker', 2),
        ]
        self._cards.extend(jokers)



