from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def select_card(self, valid_cards):
        pass

    @abstractmethod
    def bid(self):
        pass

    def get_valid_cards(self):
        pass
