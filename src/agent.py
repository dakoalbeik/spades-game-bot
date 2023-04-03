from random import choice, choices


class Agent:
    def __init__(self, version=None):
        self.version = version
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        self.hand[-1].owner = self.version
        return self

    def fetch_random_version(self):
        self.version = "agent0_0_0"

    def make_bid(self):
        possible_bids = list(range(14))
        bid_probabilities = (
            0.001213592, # Bid 0  (~0.12%)
            0.01092233,  # Bid 1  (~1.09%)
            0.071601942, # Bid 2  (~7.16%)
            0.19538835,  # Bid 3  (~19.54%)
            0.418932039, # Bid 4  (~41.89%)
            0.158398058, # Bid 5  (~15.84%)
            0.070728155, # Bid 6  (~7.07%)
            0.042475728, # Bid 7  (~4.25%)
            0.013349515, # Bid 8  (~1.33%)
            0.006067961, # Bid 9  (~0.61%)
            0.004854369, # Bid 10 (~0.49%)
            0.003640677, # Bid 11 (~0.36%)
            0.002427084, # Bid 12 (~0.24%)
            0.000000200  # Bid 13 (~0.00%)
        )
        return choices(possible_bids, bid_probabilities)[0]

    def play_card(self, leading_suit):
        selected_card = None

        # If playing the first card in the trick, any card is playable
        if leading_suit is None:
            selected_card = choice(self.hand)
        # Otherwise, begin logic to determine playable cards
        else:
            # Determine number of held cards of trick's leading suit
            num_cards_of_leading_suit = 0
            for i in range(len(self.hand)):
                if self.hand[i].suit == leading_suit:
                    num_cards_of_leading_suit += 1
            # If no cards held are of the trick's leading suit, any card is playable but only spades can win
            if num_cards_of_leading_suit == 0:
                selected_card = choice(self.hand)
            # Otherwise, create list of playable cards to choose from (i.e., list of only cards of leading suit)
            else:
                playable_cards = []
                for i in range(len(self.hand)):
                    if self.hand[i].suit == leading_suit:
                        playable_cards.append(self.hand[i])
                selected_card = choice(playable_cards)

        return selected_card

    def set_version(self, agent_version):
        self.version = agent_version

    def show_hand(self):
        for card in self.hand:
            card.show_card()
