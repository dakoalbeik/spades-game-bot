import random

from src.agents.agent import Agent


class GreedyAgent(Agent):
    NAME = "Greedy"

    def __init__(self):
        super().__init__()
        self.name = GreedyAgent.NAME

    def select_card(self, valid_cards, **kwargs):
        # TODO: write a strategy for selecting cards
        return random.choice(valid_cards)
