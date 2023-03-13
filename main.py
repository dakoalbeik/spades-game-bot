import random

# Define the deck of cards
NUM_PLAYERS = 4


def create_players():
    _players = []
    for _ in range(NUM_PLAYERS):
        player_hand = [deck.pop() for _ in range(13)]
        _players.append(player_hand)
    return _players


if __name__ == '__main__':

    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(rank, suit) for rank in ranks for suit in suits]

    # Shuffle the deck
    random.shuffle(deck)

    # Define the players
    players = create_players()

    # Define the trump suit
    trump_suit = suits[0]

    # Define the current trick
    trick = []

    # Play the game
    for round_ in range(13):
        print("Round {}".format(round_ + 1))
        for i in range(NUM_PLAYERS):
            player = players[i]
            print("Player {}'s turn".format(i + 1))
            print("Current trick: {}".format(trick))
            card = random.choice(player)
            print("Played card: {}".format(card))
            player.remove(card)
            trick.append(card)
        # Determine the winner of the trick
        winning_card = max(trick, key=lambda card: (card[1] != trump_suit, ranks.index(card[0])))
        winner_index = (trick.index(winning_card) + round_) % num_players
        print("Player {} wins the trick".format(winner_index + 1))
        trick = []
        # Update the players' scores
        players[winner_index].extend(deck[:round_ + 1])
        deck = deck[round_ + 1:]

    # Determine the winner of the game
    scores = [sum([ranks.index(card[0]) + 2 for card in player]) for player in players]
    winning_index = scores.index(max(scores))
    print("Player {} wins the game with a score of {}".format(winning_index + 1, max(scores)))


