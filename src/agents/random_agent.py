import random

from src.agents.agent import Agent


class RandomAgent(Agent):
    NAME = "Random"

    def __init__(self):
        super().__init__()

    def select_card(self, valid_cards):
        # TODO: write a strategy for selecting cards
        return random.choice(valid_cards)
