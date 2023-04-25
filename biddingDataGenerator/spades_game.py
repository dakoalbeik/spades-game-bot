import os
import string
import time
import random
from typing import List

from bot import Bot
from card import Card
from copy import deepcopy
from deck import Deck


class SpadesGame:
    MAX_ROW_CHAR_COUNT = 54
    MAX_CACHE_SIZE = MAX_ROW_CHAR_COUNT * 10_000
    MAX_HANDS_PER_FILE = 1_000_000

    def __init__(self, player_names):
        if len(player_names) != 4:
            raise ValueError("Spades requires exactly 4 players.")

        self.output_filename = ""
        self.set_random_filename()
        self.data_cache = ""
        self.hands_saved_count = 0

        self.players = [Bot(name) for name in player_names]
        self.current_actor = 0
        self.current_dealer = 0
        self.trick_history = []
        self.cards_count = 0

    def set_random_filename(self, name_length=20, data_dir='data'):
        # Create the data directory if it doesn't already exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Generate a random filename and set it as the output filename
        file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(name_length)) + '.txt'
        self.output_filename = os.path.join(data_dir, file_name)

    def deal_cards(self):
        deck = Deck()
        for player in self.players:
            player.receive_cards(deck.deal(13))

    def determine_trick_winner(self, trick):
        leading_card = trick[0]
        highest_trump_card = max((card for card in trick if card.suit == 's'),
                                 key=lambda card: Card.values.index(card.value), default=None)
        highest_lead_suit_card = max((card for card in trick if card.suit == leading_card.suit),
                                     key=lambda card: Card.values.index(card.value))

        # Compare the highest trump card and the highest lead suit card to determine the overall highest card
        if leading_card.suit != 's' and highest_trump_card:
            highest_card = highest_trump_card
        else:
            highest_card = highest_lead_suit_card

        # Update the return statement to correctly find the winner's index
        winner_index = (self.current_actor + trick.index(highest_card)) % 4
        return winner_index

    def save_hands_and_tricks(self, starting_hands, tricks_taken):

        for hand, tricks in zip(starting_hands, tricks_taken):
            hand_string = ", ".join(str(card) for card in hand)
            self.data_cache += f"{hand_string}|{tricks}\n"
            self.hands_saved_count += 1

        if len(self.data_cache) >= SpadesGame.MAX_CACHE_SIZE:
            with open(self.output_filename, "a") as f:
                f.write(self.data_cache)
            self.data_cache = ""
            print(f"Saved data and emptied cache")

        if self.hands_saved_count >= SpadesGame.MAX_HANDS_PER_FILE:
            self.set_random_filename()
            self.hands_saved_count = 0
            print("File is full, new file name is created")

    def play_trick(self):
        cards_played = []
        spades_broken = any(card.suit == "s" for trick in self.trick_history for card in trick)

        # Create deep copies of every agent's hands to simulate all remaining cards in play
        possible_cards = deepcopy(self.players[0].hand) + deepcopy(self.players[1].hand) + \
                         deepcopy(self.players[2].hand) + deepcopy(self.players[3].hand)

        i = self.current_actor
        for _ in range(4):
            chosen_card_index = self.players[i].choose_card(cards_played, spades_broken, possible_cards)
            # card = self.players[i].get_card(chosen_card_index)
            # valid_cards = SpadesGame.get_valid_cards(self.players[i].hand, cards_played, spades_broken)
            # assert len(valid_cards) > 0
            # assert card in valid_cards
            # self.cards_count += 1
            # os.system('cls')
            # print(str(self.cards_count) + "/1000000")

            card = self.players[i].play_card(chosen_card_index)
            cards_played.append(card)
            i = (i + 1) % 4
        trick_winner = self.determine_trick_winner(cards_played)
        self.current_actor = trick_winner
        self.trick_history.append(cards_played)
        return trick_winner

    @staticmethod
    def get_valid_cards(hand: List[Card], trick: List[Card], spades_broken: bool) -> List[Card]:

        leading_suit = trick[0].suit if trick else None

        # if there's a leading suit, and the player has it, then only this suit can be played
        if leading_suit:
            can_play_leading_suit = any(card.suit == leading_suit for card in hand)
            if can_play_leading_suit:
                return [card for card in hand if card.suit == leading_suit]

        # otherwise, if the player is out of the suit or spades are broken
        # or the player only has spades, allow any move
        return hand if leading_suit or spades_broken or all(
            card.suit == 's' for card in hand) else [card for card in hand if
                                                     card.suit != 's']

    def play_round(self):
        self.deal_cards()
        # Can comment out self.deal_cards() and use below lines to manually input hands. self.players[0] goes first.
        # self.players[0].hand = [Card("2", "c"), Card("8", "c"), Card("3", "d"), Card("7", "d"), Card("9", "d"), Card("2", "h"), Card("3", "h"), Card("9", "h"), Card("T", "h"), Card("J", "h"), Card("K", "h"), Card("3", "s"), Card("K", "s")]
        # self.players[1].hand = [Card("4", "c"), Card("6", "c"), Card("7", "c"), Card("K", "c"), Card("A", "c"), Card("2", "d"), Card("4", "d"), Card("K", "d"), Card("4", "h"), Card("8", "h"), Card("Q", "h"), Card("T", "s"), Card("J", "s")]
        # self.players[2].hand = [Card("5", "c"), Card("J", "c"), Card("Q", "c"), Card("5", "d"), Card("6", "d"), Card("T", "d"), Card("Q", "d"), Card("5", "h"), Card("6", "h"), Card("7", "h"), Card("5", "s"), Card("6", "s"), Card("7", "s")]
        # self.players[3].hand = [Card("3", "c"), Card("9", "c"), Card("T", "c"), Card("8", "d"), Card("J", "d"), Card("A", "d"), Card("A", "h"), Card("2", "s"), Card("4", "s"), Card("8", "s"), Card("9", "s"), Card("Q", "s"), Card("A", "s")]

        tricks_taken = [0, 0, 0, 0]

        starting_hands = [list(player.hand) for player in self.players]

        for _ in range(13):
            trick_winner = self.play_trick()
            tricks_taken[trick_winner] += 1

        # Output hands and tricks to a pipe-delimited text file
        self.save_hands_and_tricks(starting_hands, tricks_taken)

        self.current_dealer = (self.current_dealer + 1) % 4
        self.current_actor = self.current_dealer

    def play_game(self, num_rounds=10000):
        for _ in range(num_rounds):
            self.play_round()
            self.trick_history.clear()
