class CardTrick:
    def __init__(self):
        self.cards = []

    def accept_card(self, card):
        self.cards.append(card)

    @property
    def leading_suit(self):
        return self.cards[0].suit if self.cards else None

    def determine_winner(self):
        winning_card = self.cards[0]
        for i in range(1, 4):
            if (winning_card.suit != 's' and self.cards[i].suit == 's') \
                    or (winning_card.suit == self.cards[i].suit and winning_card.value < self.cards[i].value):
                winning_card = self.cards[i]
        return winning_card.owner

    def reset(self):
        self.cards.clear()
