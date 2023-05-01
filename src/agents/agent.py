from abc import ABC, abstractmethod
from src.agents.bidder import determine_bid_number


class Agent(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def select_card(self, valid_cards, **kwargs):
        pass

    def bid(self, cards):
        return max(determine_bid_number(cards), 1)
