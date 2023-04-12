from agent import Agent
import random


class GreedyAgent(Agent):

    NAME = "Greedy"

    def __init__(self):
        super().__init__()

    def select_card(self):
        pass

    def bid(self):
        return random.randint(1, 5)


