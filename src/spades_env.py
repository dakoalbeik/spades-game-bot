import random

from agents.greedy_agent import GreedyAgent
from agents.heuristic_agent import HeuristicAgent
from agents.random_agent import RandomAgent
from card_trick import CardTrick
from deck import Deck


class SpadesEnv:
    PLAYERS_NUM = 4
    MAX_TRICK_COUNT = 13
    WINNING_SCORE = 500

    def __init__(self, agents_types=None):
        self.game_over = False
        self.rounds_history = []
        self.scores = [0, 0, 0, 0]
        self.deck = Deck()
        self.trick = CardTrick()
        self.bids = [0] * 4
        self.bids_won = [0] * 4
        self.leading_bidder_idx = 0
        self.previous_trick_winner = 0

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
        self.leading_bidder_idx = random.randrange(0, SpadesEnv.PLAYERS_NUM)
        while not self.game_over:
            self.play_round()
            self.collect_scores()
            self.increment_bidder()
            self.check_game_over()
            # if (scores[0] + scores[2] >= WINNING_SCORE) or (scores[1] + scores[3] >= WINNING_SCORE):
            #     self.game_over = True

    def collect_bids(self, leading_bidder_idx):
        bids = [0] * SpadesEnv.PLAYERS_NUM
        curr_bidder = leading_bidder_idx
        for i in range(SpadesEnv.PLAYERS_NUM):
            bids[curr_bidder] = self.agents[i].bid()
            curr_bidder += 1
            curr_bidder %= SpadesEnv.PLAYERS_NUM
        self.bids = bids

    def calculate_team_score(self):
        team_scores_current_round = [0, 0]
        for i in range(2):
            target_bids = self.bids[i] + self.bids[i + 2]
            achieved_bids = self.bids_won[i] + self.bids_won[i + 2]
            if target_bids > achieved_bids:
                team_scores_current_round[i] = (target_bids * -10)
            else:
                team_scores_current_round[i] = (target_bids * 10) + achieved_bids - target_bids
        # TODO: determine what to keep from each round
        self.rounds_history.append(team_scores_current_round)
        # TODO: calculate game score

    def increment_bidder(self):
        self.leading_bidder_idx = (self.leading_bidder_idx + 1) % SpadesEnv.PLAYERS_NUM

    def collect_scores(self):

        pass

    def check_game_over(self):
        team1 = self.scores[0] + self.scores[2]
        team2 = self.scores[1] + self.scores[3]
        self.game_over = team1 >= SpadesEnv.WINNING_SCORE or team2 >= SpadesEnv.WINNING_SCORE

    def play_round(self):
        # split the deck 4 ways

        self.collect_bids()
        self.bids_won = [0] * 4
        self.previous_trick_winner = self.leading_bidder_idx
        for trick in range(SpadesEnv.MAX_TRICK_COUNT):
            self.play_trick()
            self.previous_trick_winner = self.trick.determine_winner()
            self.bids_won[self.previous_trick_winner] += 1

        # BID/PLAY ORDER:
        #  * For first round, first-to-bid is determined randomly
        #  * After first bidder, bids are taken successively [p1 -> p2 -> p3 -> p4]
        #  * Upon collection of all bids, first-to-bid plays into trick first (play proceeds to left)
        #  * Upon trick containing four cards, winner is determined and he/she is first to act in next trick
        #  * After completion of round and collection of scores, player to left of initial first-to-bid then bids first

    def play_trick(self):
        self.trick.reset()
        for i in range(SpadesEnv.PLAYERS_NUM):
            played_card = self.agents[self.previous_trick_winner].select_card()
            self.trick.accept_card(played_card)
            self.previous_trick_winner = (self.previous_trick_winner + 1) % SpadesEnv.PLAYERS_NUM

    # Playing trick:
    #  * Lead player submits card (lead suit is determined)
    #  * Next player submits card (repeat for each)
    #  * Trick class determines index of winner
    #  * Previous winner index reassigned
    #  * Point given to trick winner

    # ^^^ self.prev_winner_idx = None (or 0)
    # ...
    # def play_trick(self):
    #     ...


env = SpadesEnv()
env.play_game()
