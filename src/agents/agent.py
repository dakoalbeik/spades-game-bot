from abc import ABC, abstractmethod
from src.agents.bidder import determine_bid_number


class Agent(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def select_card(self, valid_cards):
        pass

    def bid(self, cards):
        return determine_bid_number(cards)

    def get_valid_cards(self):
        pass
