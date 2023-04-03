class StateArray:
    def __init__(self):
        # BIDDING
        self.starting_hand = []
        self.preceding_player_bids = []
        self.all_bids = []
        # ACTIVE PLAY
        self.leading_suit = ''
        self.num_cards_in_trick = 0
        self.card_to_beat = None
        self.winner_of_last_trick = None
        self.num_tricks_remaining = 13
        self.achieved_personal_bid = False
        self.achieved_team_bid = False
        self.exceeded_personal_bid = False
        # SCORING BETWEEN ROUNDS
        self.personal_score = 0
        self.team_score = 0

    def reset_all(self):
        self.starting_hand = []
        self.preceding_player_bids = []
        self.all_bids = []
        self.leading_suit = ''
        self.num_cards_in_trick = 0
        self.card_to_beat = None
        self.winner_of_last_trick = None
        self.num_tricks_remaining = 13
        self.achieved_personal_bid = False
        self.achieved_team_bid = False
        self.exceeded_personal_bid = False
        self.personal_score = 0
        self.team_score = 0

    def reset_bidding_phase_data(self):
        self.starting_hand = []
        self.preceding_player_bids = []
        self.all_bids = []

    def reset_playing_phase_data(self):
        self.leading_suit = ''
        self.num_cards_in_trick = 0
        self.card_to_beat = None
        self.winner_of_last_trick = None
        self.num_tricks_remaining = 13
        self.achieved_personal_bid = False
        self.achieved_team_bid = False
        self.exceeded_personal_bid = False

    def reset_scores(self):
        self.personal_score = 0
        self.team_score = 0

    def set_bidding_phase_data(self, learners_hand, prior_bids, complete_bids):
        self.starting_hand = learners_hand
        self.preceding_player_bids = prior_bids
        self.all_bids = complete_bids

    def set_playing_phase_data(self, lead_suit, num_cards_in_trick, leading_card, last_trick_won_by, num_tricks_remain,
                               bool_personal_bid_met, bool_team_bid_met, bool_personal_bid_exceeded):
        self.leading_suit = lead_suit
        self.num_cards_in_trick = num_cards_in_trick
        self.card_to_beat = leading_card
        self.winner_of_last_trick = last_trick_won_by
        self.num_tricks_remaining = num_tricks_remain
        self.achieved_personal_bid = bool_personal_bid_met
        self.achieved_team_bid = bool_team_bid_met
        self.exceeded_personal_bid = bool_personal_bid_exceeded

    def set_scores(self, personal_score, team_score):
        self.personal_score = personal_score
        self.team_score = team_score
