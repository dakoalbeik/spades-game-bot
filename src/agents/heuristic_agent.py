import random

from agent import Agent


class HeuristicAgent(Agent):
    NAME = "Heuristic"

    def __init__(self):
        super().__init__()

    def select_card(self, valid_cards):
        # TODO: write a strategy for selecting cards
        return random.choice(valid_cards)

    def bid(self):
        # TODO: write a strategy for bidding
        return random.randint(1, 5)
