from agent import Agent
import random


class HeuristicAgent(Agent):

    NAME = "Heuristic"

    def __init__(self):
        super().__init__()

    def select_card(self):
        pass

    def bid(self):
        return random.randint(1, 5)


