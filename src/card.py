from enum import Enum


#   D C H S
# 2 0 0 0 0
# 3 0 0 0 0
# 4 0 0 0 0
# 5 0 0 0 0
# 6 0 0 0 0
# 7 0 0 0 0
# 8 0 0 0 0
# 9 0 0 0 0
# T 0 0 0 0
# J 0 0 0 0
# Q 0 0 0 0
# K 0 0 0 0
# A 0 0 0 0
class Suit(Enum):
    SPADES = 3
    HEARTS = 2
    CLUBS = 1
    DIAMONDS = 0


SuitSymbol = {
    Suit.SPADES: "♠",
    Suit.HEARTS: "♥",
    Suit.CLUBS: "♣",
    Suit.DIAMONDS: "♦"
}


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        suit_symbol = SuitSymbol.get(self.suit)
        rank_value = self.rank.value
        rank_symbols = {
            11: "J",
            12: "Q",
            13: "K",
            14: "A"
        }
        if self.suit in [Suit.HEARTS, Suit.DIAMONDS]:
            suit_color = "\033[31m"  # Red
        else:
            suit_color = "\033[30m"  # Black
        return f"|{rank_symbols.get(rank_value, rank_value)}{suit_color}{suit_symbol}\033[0m" + " |"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __json__(self):
        return {"rank": self.rank.value, "suit": self.suit.value}

    def get_indices(self):
        return self.rank.value - 2, self.suit.value

    @staticmethod
    def from_action(action):
        # 00 - 12
        # 13 - 25
        # 26 - 38
        # 39 - 51
        rank_value = (action % 13) + 2
        suit_value = action // 13
        return Card(Rank(rank_value), Suit(suit_value))

    def to_action(self):
        return (self.rank.value - 2) + (13 * self.suit.value)
