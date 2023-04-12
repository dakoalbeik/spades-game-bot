import random

from card import Rank, Suit, Card


class Deck:
    def __init__(self):
        self.cards = []
        self.set_cards()
        self.shuffle()

    def set_cards(self):
        for suit in Suit:
            for rank in Rank:
                card = Card(rank, suit)
                self.cards.append(card)

    def __repr__(self):
        string = ''
        for card in self.cards:
            string += card.__repr__() + " "

        return string

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def reset(self):
        self.cards.clear()
        self.set_cards()
        self.shuffle()
