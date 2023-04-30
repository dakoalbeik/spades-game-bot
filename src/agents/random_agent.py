import random

from src.agents.agent import Agent


class RandomAgent(Agent):
    NAME = "Random"

    def __init__(self):
        super().__init__()
        self.name = RandomAgent.NAME

    def select_card(self, valid_cards, **kwargs):
        return random.choice(valid_cards)
