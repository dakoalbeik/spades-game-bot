from agent import Agent
import random


class RandomAgent(Agent):
    NAME = "Random"

    def __init__(self):
        super().__init__()

    def select_card(self):
        pass

    def bid(self):
        return random.randint(1, 5)
