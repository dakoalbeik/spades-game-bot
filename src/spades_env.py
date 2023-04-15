import random
from typing import List

from agents.greedy_agent import GreedyAgent
from agents.heuristic_agent import HeuristicAgent
from agents.random_agent import RandomAgent
from card_trick import CardTrick
from deck import Deck
from deck.card import Suit, Card


class SpadesEnv:
    PLAYERS_NUM = 4
    MAX_TRICK_COUNT = 13
    WINNING_SCORE = 500
    NIL = 0

    def __init__(self, agents_types=None):

        self.game_over = False
        self.rounds_history = []
        self.scores = [0] * 4
        self.deck = Deck()
        self.trick = CardTrick()
        self.bids = [0] * 4
        self.tricks_won = [0] * 4
        self.leading_bidder_idx = 0
        self.previous_trick_winner = 0
        self.spades_broken = False
        self.agents = []
        self.hands = [[]] * 4
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

    def collect_bids(self):
        for i in range(SpadesEnv.PLAYERS_NUM):
            self.bids[i] = self.agents[(self.leading_bidder_idx + i) % SpadesEnv.PLAYERS_NUM].bid()

    def calculate_team_round_score(self):
        round_scores = [0, 0]
        round_bags = [0, 0]
        SpadesEnv.NIL = 0

        for i in range(4):
            # if player goes SpadesEnv.NIL
            team_mate = (i + 2) % 4
            curr_score = i % 2
            if self.bids[i] == SpadesEnv.NIL:
                if self.tricks_won[i] == 0:
                    round_scores[curr_score] += 100
                else:
                    round_scores[curr_score] -= 100
                    round_bags[curr_score] += self.tricks_won[i]
            # if player bid, and the score for the team is getting set for the first time, or the teammate bid nil
            # (meaning the current score doesn't account for this current player's score)
            elif round_scores[curr_score] == 0 or self.bids[team_mate] == SpadesEnv.NIL:
                team_target_bids = self.bids[i] + self.bids[team_mate]
                team_trick_count = self.tricks_won[i] + self.tricks_won[team_mate]
                if team_trick_count < team_target_bids:
                    round_scores[curr_score] -= team_target_bids * 10
                else:
                    round_scores[curr_score] += team_target_bids * 10
                    if self.bids[team_mate] == SpadesEnv.NIL:
                        round_bags[curr_score] += self.tricks_won[i] - self.bids[i]
                    else:
                        round_bags[curr_score] += team_trick_count - team_target_bids

        return round_scores, round_bags

    def increment_bidder(self):
        self.leading_bidder_idx = (self.leading_bidder_idx + 1) % SpadesEnv.PLAYERS_NUM

    def collect_scores(self):

        pass

    def check_game_over(self):
        team1 = self.scores[0] + self.scores[2]
        team2 = self.scores[1] + self.scores[3]
        self.game_over = team1 >= SpadesEnv.WINNING_SCORE or team2 >= SpadesEnv.WINNING_SCORE

    def play_round(self):
        # TODO 01: split the deck 4 ways
        self.collect_bids()
        self.tricks_won = [0] * 4
        self.previous_trick_winner = self.leading_bidder_idx
        for trick in range(SpadesEnv.MAX_TRICK_COUNT):
            self.play_trick()
            self.previous_trick_winner = self.trick.determine_winner()
            self.tricks_won[self.previous_trick_winner] += 1

    def play_trick(self):
        self.trick.reset()
        for i in range(SpadesEnv.PLAYERS_NUM):
            played_card = self.agents[self.previous_trick_winner].select_card()
            if played_card.suit.value == Suit.SPADES:
                self.spades_broken = True
            self.trick.accept_card(played_card)
            self.previous_trick_winner = (self.previous_trick_winner + 1) % SpadesEnv.PLAYERS_NUM

    def get_valid_cards(self, player_index: int) -> List[Card]:
        """
        Loops over the given players hand and returns a list of the possible cards to be played
        :param player_index
        :return: List of valid cards
        """
        player_hand = self.hands[player_index]
        leading_suit = self.trick.leading_suit

        # if there's a leading suit, and the player has it, then only this suit can be played
        if leading_suit:
            can_play_leading_suit = any(card.suit == leading_suit for card in player_hand)
            if can_play_leading_suit:
                return [card for card in player_hand if card.suit == leading_suit]

        # otherwise, if the player is out of the suit or spades are broken
        # or the player only has spades, allow any move
        return player_hand if not leading_suit or self.spades_broken or all(
            card.suit == Suit.SPADES for card in player_hand) else [card for card in player_hand if
                                                                    card.suit != Suit.SPADES]
