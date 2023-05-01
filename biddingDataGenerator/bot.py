# from card import Card
#
#
# class Bot:
#     def __init__(self, name):
#         self.name = name
#         self.hand = []
#
#     def choose_card(self, trick, spades_broken, possible_cards):
#         if len(trick) == 0:
#             return self.first_to_act(spades_broken, possible_cards)
#         elif len(trick) == 1:
#             return self.second_to_act(trick[0], possible_cards)
#         elif len(trick) == 2:
#             return self.third_to_act(trick, possible_cards)
#         else:
#             return self.last_to_act(trick)
#
#     def first_to_act(self, spades_broken, possible_cards):
#         # Can play any suit unless spades not broken. If spades not broken, then all suits except spades playable.
#         legal_suits = Card.suits if spades_broken else [suit for suit in Card.suits if suit != 's']
#
#         # Find the highest value card for each legal suit in remaining possible cards. By remaining possible cards, we
#         # mean the cards which have not yet been played into the current trick or a previous trick.
#         max_values = {suit: max(possible_cards, key=lambda card: (card.suit == suit, Card.values.index(card.value))) for
#                       suit in legal_suits}
#
#         # Return hand card equal to a card from max_values. If no such card in hand, return None.
#         max_value_card = next((card for card in self.hand if any(card.suit == max_card.suit and card.value ==
#                                                                  max_card.value for max_card in max_values.values())),
#                               None)
#         if max_value_card:
#             return self.hand.index(max_value_card)
#
#         # Since no max_value_card was found, we will play a burn card from the least represented suit. First, count the
#         # number of cards per suit.
#         suit_counts = {suit: sum(1 for card in self.hand if card.suit == suit) for suit in legal_suits}
#
#         # Because we want to exhaust non-trump suits in order to play trumps earlier in the round, we do not want to
#         # count spades as our least represented suit. However, if we only have spades in our hand, we MUST play a spade.
#         if all(card.suit == 's' for card in self.hand):
#             least_represented_suit = 's'
#         else:
#             least_represented_suit = min((suit for suit in suit_counts if suit_counts[suit] > 0 and suit != 's'),
#                                          key=suit_counts.get)
#
#         # Fetch the lowest value card of the least represented suit.
#         lowest_card_of_suit = min((card for card in self.hand if card.suit == least_represented_suit),
#                                   key=lambda card: Card.values.index(card.value))
#         return self.hand.index(lowest_card_of_suit)
#
#     def last_to_act(self, trick):
#         # Note all cards in the trick and the suit of the first card in the trick (lead suit).
#         lead_card, second_card, third_card = trick
#         lead_suit = lead_card.suit
#
#         # Determine the currently winning card in the trick.
#         winning_card = lead_card
#         for card in [second_card, third_card]:
#             if card.suit == winning_card.suit and Card.values.index(card.value) > Card.values.index(winning_card.value):
#                 winning_card = card
#             elif card.suit == 's' and winning_card.suit != 's':
#                 winning_card = card
#
#         # Check if there's a card of the lead suit that can beat the winning card. If more than one such card exists,
#         # play the lowest value card and reserve the stronger cards for later tricks.
#         lead_suit_cards = [card for card in self.hand if card.suit == lead_suit]
#         if lead_suit_cards:
#             winning_lead_suit_cards = [card for card in lead_suit_cards if Card.values.index(card.value) >
#                                        Card.values.index(winning_card.value)]
#             if winning_lead_suit_cards:
#                 lowest_winning_card = min(winning_lead_suit_cards, key=lambda card: Card.values.index(card.value))
#                 return self.hand.index(lowest_winning_card)
#
#             # Play the lowest value card of the lead suit if no winning card is available.
#             lowest_card_of_suit = min(lead_suit_cards, key=lambda card: Card.values.index(card.value))
#             return self.hand.index(lowest_card_of_suit)
#
#         spades_cards = [card for card in self.hand if card.suit == 's']
#
#         # If we have no cards of the lead suit in our hand, search for the minimally valued, winning spade.
#         if spades_cards:
#             if winning_card.suit == 's':
#                 higher_spades_cards = [card for card in spades_cards if Card.values.index(card.value) >
#                                        Card.values.index(winning_card.value)]
#                 if higher_spades_cards:
#                     min_winning_spades_card = min(higher_spades_cards, key=lambda card: Card.values.index(card.value))
#                     return self.hand.index(min_winning_spades_card)
#             else:
#                 min_spades_card = min(spades_cards, key=lambda card: Card.values.index(card.value))
#                 return self.hand.index(min_spades_card)
#
#         # If no winning spade, play the lowest card of the least represented suit.
#         legal_suits = [suit for suit in Card.suits if suit != 's' and suit != lead_suit]
#         suit_counts = {suit: sum(1 for card in self.hand if card.suit == suit) for suit in legal_suits}
#
#         # If hand contains only spades, play the lowest value spade.
#         if all(card.suit == 's' for card in self.hand):
#             lowest_spade = min(self.hand, key=lambda card: Card.values.index(card.value))
#             return self.hand.index(lowest_spade)
#         # Else, play the lowest value card of the least represented non-trump suit.
#         else:
#             least_represented_suit = min((suit for suit in suit_counts if suit_counts[suit] > 0), key=suit_counts.get)
#             lowest_card_of_suit = min((card for card in self.hand if card.suit == least_represented_suit),
#                                       key=lambda card: Card.values.index(card.value))
#             return self.hand.index(lowest_card_of_suit)
#
#     def play_card(self, card_index):
#         return self.hand.pop(card_index)
#
#     def get_card(self, index):
#         return self.hand[index]
#
#     def receive_cards(self, cards):
#         self.hand.extend(cards)
#         self.hand.sort(key=lambda card: (Card.suits.index(card.suit), Card.values.index(card.value)))
#
#     def second_to_act(self, lead_card, possible_cards):
#         # Note the lead suit and list all cards of the lead suit.
#         lead_suit = lead_card.suit
#         lead_suit_cards = [card for card in self.hand if card.suit == lead_suit]
#
#         # If we do not have any cards of the lead suit, we will look next for spades.
#         spades_cards = [card for card in self.hand if card.suit == 's']
#
#         # If we have cards of the lead suit, search for the max value card from all possible remaining cards. If we have
#         # this max card and the max card beats the card in the current trick, play it.
#         if lead_suit_cards:
#             max_possible_card = max([card for card in possible_cards if card.suit == lead_suit],
#                                     key=lambda card: Card.values.index(card.value), default=None)
#             max_hand_card = max(lead_suit_cards, key=lambda card: Card.values.index(card.value))
#
#             if (max_hand_card.value == max_possible_card.value and max_hand_card.suit == max_possible_card.suit) and \
#                     Card.values.index(max_hand_card.value) > Card.values.index(lead_card.value):
#                 return self.hand.index(max_hand_card)
#
#             # If the max card for the lead suit does not exist in our hand, play the lowest value card of the lead suit.
#             min_lead_suit_card = min(lead_suit_cards, key=lambda card: Card.values.index(card.value))
#             return self.hand.index(min_lead_suit_card)
#
#         # If we have no cards of the lead suit, play the lowest value spade.
#         if spades_cards:
#             min_spades_card = min(spades_cards, key=lambda card: Card.values.index(card.value))
#             return self.hand.index(min_spades_card)
#
#         # If we have neither cards of the lead suit nor spades, determine which of the remaining two suits for which we
#         # have the fewest cards. We look for the least represented non-trump suit and play the lowest value card.
#         legal_suits = [suit for suit in Card.suits if suit != 's' and suit != lead_suit]
#         suit_counts = {suit: sum(1 for card in self.hand if card.suit == suit) for suit in legal_suits}
#         least_represented_suit = min((suit for suit in suit_counts if suit_counts[suit] > 0), key=suit_counts.get)
#
#         lowest_card_of_suit = min((card for card in self.hand if card.suit == least_represented_suit),
#                                   key=lambda card: Card.values.index(card.value))
#         return self.hand.index(lowest_card_of_suit)
#
#     def third_to_act(self, trick, possible_cards):
#         # Note the two cards in the trick, the suit of the first card (lead suit), and make a list of hand cards of the
#         # lead suit and a list of spades in our hand.
#         lead_card, second_card = trick
#         lead_suit = lead_card.suit
#         lead_suit_cards = [card for card in self.hand if card.suit == lead_suit]
#         spades_cards = [card for card in self.hand if card.suit == 's']
#
#         # Determine the currently winning card in the trick.
#         if second_card.suit == lead_suit:
#             winning_card = max(lead_card, second_card, key=lambda card: Card.values.index(card.value))
#         elif second_card.suit == 's':
#             winning_card = second_card
#         else:
#             winning_card = lead_card
#
#         # If we have cards of the lead suit, search for the max value card of the lead suit. If it exists in our hand,
#         # play it. Else, play the lowest value card from our hand of the lead suit.
#         if lead_suit_cards:
#             max_possible_card = max([card for card in possible_cards if card.suit == lead_suit],
#                                     key=lambda card: Card.values.index(card.value), default=None)
#             max_hand_card = max(lead_suit_cards, key=lambda card: Card.values.index(card.value))
#
#             if (max_hand_card.value == max_possible_card.value and max_hand_card.suit == max_possible_card.suit) and \
#                     Card.values.index(max_hand_card.value) > Card.values.index(lead_card.value):
#                 return self.hand.index(max_hand_card)
#
#             min_lead_suit_card = min(lead_suit_cards, key=lambda card: Card.values.index(card.value))
#             return self.hand.index(min_lead_suit_card)
#
#         # If we have no cards of the lead suit in our hand, search for the minimally valued, winning spade.
#         if spades_cards:
#             if winning_card.suit == 's':
#                 higher_spades_cards = [card for card in spades_cards if Card.values.index(card.value) >
#                                        Card.values.index(winning_card.value)]
#                 if higher_spades_cards:
#                     min_winning_spades_card = min(higher_spades_cards, key=lambda card: Card.values.index(card.value))
#                     return self.hand.index(min_winning_spades_card)
#             else:
#                 min_spades_card = min(spades_cards, key=lambda card: Card.values.index(card.value))
#                 return self.hand.index(min_spades_card)
#
#         # If our hand has neither lead-suit cards or winning spades, determine the least represented suit in hand and
#         # play the lowest value card from our hand of that suit.
#         legal_suits = [suit for suit in Card.suits if suit != 's' and suit != lead_suit]
#         suit_counts = {suit: sum(1 for card in self.hand if card.suit == suit) for suit in legal_suits}
#
#         if all(card.suit == 's' for card in self.hand):
#             lowest_spade = min(self.hand, key=lambda card: Card.values.index(card.value))
#             return self.hand.index(lowest_spade)
#         # Else, play the lowest value card of the least represented non-trump suit.
#         else:
#             least_represented_suit = min(
#                 (suit for suit in suit_counts if suit_counts[suit] > 0), key=suit_counts.get)
#             lowest_card_of_suit = min((card for card in self.hand if card.suit == least_represented_suit),
#                                       key=lambda card: Card.values.index(card.value))
#             return self.hand.index(lowest_card_of_suit)
