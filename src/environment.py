from agent_storage import AgentStorage
from card_trick import CardTrick
from deck import Deck
from random import choice, randint
from state_array import StateArray
from time import sleep


class Environment:
    def __init__(self, learner):
        self.agents = AgentStorage()
        self.bool_game_finished = False
        self.completed_tricks = 0
        self.current_trick = CardTrick()
        self.deck_of_cards = Deck()
        self.outgoing_state = StateArray()
        self.players = []
        self.player_bids = [0, 0, 0, 0]
        self.player_tricks_won = [0, 0, 0, 0]
        self.scores_current_round = [0, 0, 0, 0]
        self.scores_game_total = [0, 0, 0, 0]
        self.team_scores_current_round = [0, 0]
        self.team_scores_game_total = [0, 0]

        print('Initializing environment . . .')
        sleep(1)

        # Select learning agents and three other agents
        self.select_agents(learner)
        print('Agents selected')
        sleep(1)

        # Select random agents to go first for first round.
        # Round concludes when 13 tricks are played.
        # As in real life, the player to the dealer's left (i.e., next player in list players) will lead the next round.
        index_of_leading_player = randint(0, 3)

        # Repeat until team obtains 200 points.
        # Each loop is the start of a new round of play.
        round_number = 1
        while not self.bool_game_finished:
            # Shuffle deck and deal cards
            self.deck_of_cards.reset()
            self.generate_starting_hands(self.deck_of_cards)
            print('Deck shuffled and starting hands distributed')
            sleep(1)

            # Start bidding
            bidding_index = index_of_leading_player
            bids_made = 0
            while bids_made < 4:
                if bidding_index == 0:
                    # OUTPUT STATE: Learner receives info regarding own hand and any bids made by preceding players
                    self.generate_state(None)
                self.player_bids[bidding_index] = self.players[bidding_index].make_bid()
                bidding_index = (bidding_index + 1) % 4
                bids_made += 1
            print('Collected bids:')
            for i in range(4):
                print('  {}: {}'.format(self.players[i].version, self.player_bids[i]))
            sleep(1)

            # Repeat until 13 tricks completed
            # i = leading player, but it will take the value of the trick winner with each loop iteration below.
            i = index_of_leading_player
            cards_played = 0
            while self.completed_tricks <= 13:
                while len(self.current_trick.cards) < 4:
                    # Agent in players at index i selects a card to submit
                    submitted_card = self.players[i].play_card(self.current_trick.leading_suit)
                    self.current_trick.accept_card(submitted_card)

                    # Move to next player in list (loop to index 0 when necessary)
                    i = (i + 1) % 4
                    cards_played += 1

                # With four cards in the trick, determine winner
                trick_winner = self.current_trick.determine_winner()
                for i in range(len(self.players)):
                    if self.players[i].version == trick_winner:
                        self.player_tricks_won[i] += 1
                self.completed_tricks += 1

                # Reset trick data
                self.current_trick.reset()

            # Calculate scores
            self.calculate_individual_score()
            self.calculate_team_score()

            # When team reaches 200 points, game is finished
            for i in range(2):
                if self.team_scores_game_total[i] >= 200:
                    self.bool_game_finished = True

            # Print scores and increment round number
            self.print_scores(round_number)
            round_number += 1

            self.reset_round_scores()

            # Next player in list leads the next round of play
            index_of_leading_player = (index_of_leading_player + 1) % 4

    def calculate_individual_score(self):
        for i in range(4):
            if self.player_bids[i] > self.player_tricks_won[i]:
                self.scores_current_round[i] -= (self.player_bids[i] * 10)
            else:
                # 10 points for each bid win plus 1 point for any tricks won in addition to bid
                self.scores_current_round[i] += ((self.player_bids[i] * 10) + max(0, self.scores_current_round[i]\
                                                 - self.player_bids[i]))

    def calculate_team_score(self):
        for i in range(2):
            if (self.player_bids[i] + self.player_bids[i + 2]) > (self.player_tricks_won[i] + self.player_tricks_won[i + 2]):
                self.team_scores_current_round[i] -= ((self.player_bids[i] + self.player_bids[i + 2]) * 10)
            else:
                self.team_scores_current_round[i] += ((self.player_bids[i] + self.player_bids[i + 2]) * 10) + max(0, (self.scores_current_round[i] + self.scores_current_round[i + 2] - self.player_bids[i] - self.player_bids[i]))

    def generate_starting_hands(self, card_deck):
        for i in range(len(self.players)):
            for j in range(13):
                self.players[i].draw_card(card_deck)

    def generate_state(self, action):
        # STARTING HAND: Should update only at the beginning of the game.
        # BIDS OF PREVIOUS PLAYERS: Should update immediately prior to the learner's turn to bid.
        # ALL BIDS: Should update only after all bids have been made.
        # LEADING SUIT OF CURRENT TRICK
        # NUMBER OF CARDS IN CURRENT TRICK
        # CARD TO BEAT IN CURRENT TRICK
        # WINNER OF PREVIOUS TRICK
        # NUMBER OF REMAINING TRICKS IN ROUND
        # ACHIEVED PERSONAL BID?
        # ACHIEVED TEAM BID?
        # PERSONAL SCORE
        # TEAM SCORE
        pass

    def print_scores(self, round_number):
        print('Round {}:'.format(round_number))
        print(' Individual scores:')
        for i in range(len(self.players)):
            print('  {}: {}'.format(self.players[i].version, self.scores_current_round[i]))
        print(' Team scores:')
        for i in range(len(self.team_scores_current_round)):
            print('  Team {}: {}'.format(i, self.team_scores_current_round[i]))

    def reset_round_scores(self):
        self.player_bids = [0, 0, 0, 0]
        self.scores_current_round = [0, 0, 0, 0]
        self.team_scores_current_round = [0, 0]

    def select_agents(self, learner):
        self.players.append(learner)
        for i in range(3):
            self.players.append(choice(self.agents.idiot_agents))
