from card import Card
from random import shuffle
from itertools import product


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value, suit in product(Card.values, Card.suits)]
        shuffle(self.cards)

    def deal(self, n):
        return [self.cards.pop() for _ in range(n)]
