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
        highest_card = self.cards[0]
        winning_player = 0
        lead_suit = self.leading_suit

        # Iterate over the cards and find the highest card
        for i, card in enumerate(self.cards):
            is_greater_rank = card.rank.value > highest_card.rank.value
            no_spade = highest_card.suit != Suit.SPADES
            # If card is greater spade
            if card.suit == Suit.SPADES and (no_spade or is_greater_rank):
                highest_card = card
                winning_player = i

            # If card is greater lead suit
            elif no_spade and card.suit == lead_suit and is_greater_rank:
                highest_card = card
                winning_player = i

        return (winning_player + lead_player) % 4

    def reset(self):
        self.cards.clear()
