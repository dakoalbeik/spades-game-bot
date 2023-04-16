import random
import time
from typing import List

from src.agents.greedy_agent import GreedyAgent
from src.agents.heuristic_agent import HeuristicAgent
from src.agents.random_agent import RandomAgent
from src.card import Suit, Card
from src.card_trick import CardTrick
from src.deck import Deck


def _print(msg, p=True):
    if not p:
        return
    else:
        print(msg)


class SpadesEnv:
    MAX_BAGS = 10
    TRICK_WORTH = 10
    NIL_WORTH = 100
    WINNING_SCORE = 500
    TEAMS = True
    PLAYERS_NUM = 4
    TRICKS_COUNT = 13
    NIL = 0

    def __init__(self, teams=True, max_score=500, agents_types=None, emit=None):
        SpadesEnv.TEAMS = teams
        SpadesEnv.WINNING_SCORE = max_score
        self.game_over = False
        self.rounds_history = []
        self.scores = [0] * (SpadesEnv.PLAYERS_NUM // 2) if teams else [0] * SpadesEnv.PLAYERS_NUM
        self.bags = [0] * (SpadesEnv.PLAYERS_NUM // 2) if teams else [0] * SpadesEnv.PLAYERS_NUM
        self.deck = Deck()
        self.trick = CardTrick()
        self.bids = [0] * SpadesEnv.PLAYERS_NUM
        self.tricks_won = [0] * SpadesEnv.PLAYERS_NUM
        self.leading_bidder_idx = 0
        self.previous_trick_winner = 0
        self.spades_broken = False
        self.agents = []
        self.hands = [[], [], [], []]
        self.init_agents(agents_types)
        self.emit = emit

    def update_gui(self, duration=2.5):
        if self.emit:
            self.emit({
                "scores": self.scores,
                "bags": self.bags,
                "trick": [card.__json__() for card in self.trick.cards],
                "bids": self.bids,
                "tricks_won": self.tricks_won,
                "spades_broken": self.spades_broken,
                "hands": [[card.__json__() for card in hand] for hand in self.hands],
            })
            time.sleep(duration)

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

    def deal_cards(self):
        self.deck.shuffle()
        for i in range(SpadesEnv.TRICKS_COUNT):
            for j in range(SpadesEnv.PLAYERS_NUM):
                self.hands[j].append(self.deck.draw_card())

    def collect_bids(self):
        for i in range(SpadesEnv.PLAYERS_NUM):
            self.bids[i] = self.agents[(self.leading_bidder_idx + i) % SpadesEnv.PLAYERS_NUM].bid()

    def calculate_team_round_score(self):
        round_scores = [0, 0]
        round_bags = [0, 0]

        for i in range(SpadesEnv.PLAYERS_NUM):
            # if player goes SpadesEnv.NIL
            team_mate = (i + 2) % SpadesEnv.PLAYERS_NUM
            curr_score = i % 2
            if self.bids[i] == SpadesEnv.NIL:
                if self.tricks_won[i] == 0:
                    round_scores[curr_score] += SpadesEnv.NIL_WORTH
                else:
                    round_scores[curr_score] -= SpadesEnv.NIL_WORTH
                    round_bags[curr_score] += self.tricks_won[i]
            # if player bid, and the score for the team is getting set for the first time, or the teammate bid nil
            # (meaning the current score doesn't account for this current player's score)
            elif round_scores[curr_score] == 0 or self.bids[team_mate] == SpadesEnv.NIL:
                team_target_bids = self.bids[i] + self.bids[team_mate]
                team_trick_count = self.tricks_won[i] + self.tricks_won[team_mate]
                if team_trick_count < team_target_bids:
                    round_scores[curr_score] -= team_target_bids * SpadesEnv.TRICK_WORTH
                else:
                    round_scores[curr_score] += team_target_bids * SpadesEnv.TRICK_WORTH
                    if self.bids[team_mate] == SpadesEnv.NIL:
                        round_bags[curr_score] += self.tricks_won[i] - self.bids[i]
                    else:
                        round_bags[curr_score] += team_trick_count - team_target_bids

        return round_scores, round_bags

    def increment_bidder(self):
        self.leading_bidder_idx = (self.leading_bidder_idx + 1) % SpadesEnv.PLAYERS_NUM

    def collect_scores(self):
        if SpadesEnv.TEAMS:
            round_scores, round_bags = self.calculate_team_round_score()
            for i in range(2):
                self.scores[i] += round_scores[i]
                self.bags[i] += round_bags[i]

                if self.bags[i] >= SpadesEnv.MAX_BAGS:
                    self.scores[i] -= SpadesEnv.MAX_BAGS * SpadesEnv.TRICK_WORTH
                    self.bags[i] -= SpadesEnv.MAX_BAGS
        else:
            self.calculate_solo_round_score()

    def check_game_over(self):
        if SpadesEnv.TEAMS:
            self.game_over = self.scores[0] >= SpadesEnv.WINNING_SCORE or self.scores[1] >= SpadesEnv.WINNING_SCORE
        else:
            pass

    def play_game(self):
        print("start game")
        self.leading_bidder_idx = random.randrange(0, SpadesEnv.PLAYERS_NUM)
        while not self.game_over:
            self.play_round()
            self.spades_broken = False
            self.collect_scores()
            self.increment_bidder()
            self.check_game_over()
            self.update_gui()
            print(self.scores)

    def play_round(self):
        self.deal_cards()
        self.collect_bids()
        self.tricks_won = [0] * 4
        self.update_gui()
        self.previous_trick_winner = self.leading_bidder_idx
        for trick in range(SpadesEnv.TRICKS_COUNT):
            self.play_trick()
            self.update_gui()

    def play_trick(self):
        self.trick.reset()
        for i in range(SpadesEnv.PLAYERS_NUM):
            self.play_card((self.previous_trick_winner + i) % SpadesEnv.PLAYERS_NUM)
        self.previous_trick_winner = self.trick.determine_winner(self.previous_trick_winner)
        self.tricks_won[self.previous_trick_winner] += 1

    def play_card(self, player_idx):
        valid_cards = self.get_valid_cards(player_idx)
        played_card = self.agents[player_idx].select_card(valid_cards)
        self.trick.accept_card(played_card)
        self.deck.add_card(played_card)
        self.hands[player_idx].remove(played_card)
        if played_card.suit == Suit.SPADES:
            self.spades_broken = True
        self.update_gui()

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

    def calculate_solo_round_score(self):
        pass
