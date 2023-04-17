from src.card import Suit


class CardTrick:
    def __init__(self):
        self.cards = []

    def accept_card(self, card):
        self.cards.append(card)

    @property
    def leading_suit(self):
        return self.cards[0].suit if self.cards else None

    def determine_winner(self, lead_player):
        # Initialize variables to store the highest card and player index
        highest_card = self.cards[0]
        highest_player = 0

        # Iterate over the cards and find the highest card
        for i in range(len(self.cards)):
            card = self.cards[i]
            suit = card.suit

            # Check if the card is a trump card
            if suit == Suit.SPADES and card.rank.value > highest_card.rank.value:
                highest_card = card
                highest_player = i

            # Check if the card is the highest of the leading suit
            elif suit == self.leading_suit and card.rank.value > highest_card.rank.value:
                highest_card = card
                highest_player = i

        # Account for the lead player index
        winning_player = (highest_player + lead_player) % 4

        return winning_player

    def reset(self):
        self.cards.clear()
