import random

from card import Rank, Suit, Card


class Deck:
    def __init__(self):
        self.cards = []
        self.set_full_deck()
        self.shuffle()

    def set_full_deck(self):
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

    def add_card(self, card):
        self.cards.append(card)

    def reset(self):
        self.cards.clear()
        self.set_full_deck()
        self.shuffle()
