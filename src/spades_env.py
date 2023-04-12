import random

from agents.greedy_agent import GreedyAgent
from agents.heuristic_agent import HeuristicAgent
from agents.random_agent import RandomAgent


class SpadesEnv:
    PLAYERS_NUM = 4
    MAX_TRICK_COUNT = 13

    def __init__(self, agents_types=None):
        self.game_over = False
        self.rounds_history = []
        self.scores = [0, 0, 0, 0]

        self.agents = []
        self.init_agents(agents_types)

    def init_agents(self, agents_types):
        if agents_types is None:  # Default to RandomAgent
            agents_types = [RandomAgent.NAME] * SpadesEnv.PLAYERS_NUM
        elif isinstance(agents_types, str):  # Single agent type
            agents_types = [agents_types] * SpadesEnv.PLAYERS_NUM
        elif len(agents_types) != SpadesEnv.PLAYERS_NUM:
            raise ValueError(f"Players count should be {SpadesEnv.PLAYERS_NUM}")

        for i in range(SpadesEnv.PLAYERS_NUM):
            if agents_types[i] == RandomAgent.NAME:
                self.agents.append(RandomAgent())
            elif agents_types[i] == HeuristicAgent.NAME:
                self.agents.append(HeuristicAgent())
            elif agents_types[i] == GreedyAgent.NAME:
                self.agents.append(GreedyAgent())

    def play_game(self):
        while not self.game_over:
            leading_bidder_idx = random.randrange(0, SpadesEnv.PLAYERS_NUM)
            self.play_round(leading_bidder_idx)
            self.game_over = True

    def play_round(self, leading_bidder_idx):
        bids = [0] * SpadesEnv.PLAYERS_NUM
        curr_bidder = leading_bidder_idx
        for i in range(SpadesEnv.PLAYERS_NUM):
            bids[curr_bidder] = self.agents[i].bid()
            curr_bidder += 1
            curr_bidder %= SpadesEnv.PLAYERS_NUM

        for hand in range(SpadesEnv.MAX_TRICK_COUNT):


    def play_hand(self, leading_player_idx):
        pass


env = SpadesEnv()
env.play_game()
