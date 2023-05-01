class Card:
    suits = "cdhs"
    values = "23456789TJQKA"

    def __init__(self, value, suit):
        if value not in Card.values or suit not in Card.suits:
            raise ValueError("Invalid card value or suit")
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.value}{self.suit}"
