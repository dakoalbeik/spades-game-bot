class CardTrick:
    def __init__(self):
        self.leading_suit = None
        self.cards = []

    def accept_card(self, card):
        if self.leading_suit is None:
            self.leading_suit = card.suit
        self.cards.append(card)

    def determine_winner(self):
        winning_card = self.cards[0]
        for i in range(1, 4):
            if (winning_card.suit != 's' and self.cards[i].suit == 's')\
                    or (winning_card.suit == self.cards[i].suit and winning_card.value < self.cards[i].value):
                winning_card = self.cards[i]
        return winning_card.owner

    def reset(self):
        self.leading_suit = None
        self.cards.clear()
