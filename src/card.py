class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.owner = None

    def show_card(self):
        display_name_by_value = {
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'A',
        }
        if display_name_by_value.get(self.value):
            print("{}{}".format(display_name_by_value.get(self.value), self.suit), end=' ')
        else:
            print("{}{}".format(self.value, self.suit), end=' ')
