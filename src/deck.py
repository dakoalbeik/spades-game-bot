from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.create_cards()
        self.shuffle_deck()

    def create_cards(self):
        for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            for suit in ['c', 'd', 'h', 's']:
                self.cards.append(Card(value, suit))

    def display_cards(self):
        for card in self.cards:
            card.show_card()

    def draw_card(self):
        return self.cards.pop()

    def reset(self):
        self.cards.clear()
        self.create_cards()
        self.shuffle_deck()

    def shuffle_deck(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
