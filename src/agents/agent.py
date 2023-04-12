from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self):
        self.hand = []
        self.name = ""

    @abstractmethod
    def select_card(self):
        pass

    @abstractmethod
    def bid(self):
        pass

    def get_valid_cards(self):
        pass

