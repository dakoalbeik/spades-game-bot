from src.card import Suit, Rank, Card

c = [
    Card(Rank.TWO, Suit.CLUBS),
    Card(Rank.SIX, Suit.CLUBS),
    Card(Rank.SEVEN, Suit.CLUBS),
    Card(Rank.NINE, Suit.DIAMONDS),
    Card(Rank.TEN, Suit.DIAMONDS),
    Card(Rank.QUEEN, Suit.DIAMONDS),
    Card(Rank.ACE, Suit.DIAMONDS),
    Card(Rank.THREE, Suit.HEARTS),
    Card(Rank.SIX, Suit.HEARTS),
    Card(Rank.TEN, Suit.HEARTS),
    Card(Rank.KING, Suit.HEARTS),
    Card(Rank.FOUR, Suit.SPADES),
    Card(Rank.KING, Suit.SPADES),
]


def determine_bid_number(cards):
    num_spades = 0
    sum_spades_values = 0
    num_nt_aces = 0
    num_nt_kings = 0
    suit_count = {suit: 0 for suit in Suit}

    for card in cards:
        suit_count[card.suit] += 1

        if card.suit == Suit.SPADES:
            num_spades += 1
            sum_spades_values += card.rank.value

        if card.rank == Rank.ACE and card.suit != Suit.SPADES:
            num_nt_aces += 1

        if card.rank == Rank.KING and card.suit != Suit.SPADES:
            num_nt_kings += 1

    num_void_suits = sum(1 for suit, count in suit_count.items() if count == 0 and suit != Suit.SPADES)

    if num_spades <= 5.50:
        if sum_spades_values <= 24.50:
            if num_nt_aces <= 1.50:
                if num_spades <= 1.50:
                    if num_nt_aces <= 0.50:
                        if sum_spades_values <= 11.50:
                            if num_nt_kings <= 1.50:
                                if sum_spades_values <= 10.50:
                                    if sum_spades_values <= 4.50:
                                        if num_nt_kings <= 0.50:
                                            if num_void_suits <= 0.50:
                                                return 0.0
                                            if num_void_suits > 0.50:
                                                return 1.0
                                        if num_nt_kings > 0.50:
                                            return 1.0
                                    if sum_spades_values > 4.50:
                                        if num_nt_kings <= 0.50:
                                            if num_void_suits <= 0.50:
                                                return 0.0
                                            if num_void_suits > 0.50:
                                                return 1.0
                                        if num_nt_kings > 0.50:
                                            return 1.0
                                if sum_spades_values > 10.50:
                                    return 1.0
                            if num_nt_kings > 1.50:
                                if sum_spades_values <= 1.00:
                                    return 1.0
                                if sum_spades_values > 1.00:
                                    if num_void_suits <= 0.50:
                                        if num_nt_kings <= 2.50:
                                            if sum_spades_values <= 8.50:
                                                return 1.0
                                            if sum_spades_values > 8.50:
                                                return 2.0
                                        if num_nt_kings > 2.50:
                                            return 2.0
                                    if num_void_suits > 0.50:
                                        return 2.0
                        if sum_spades_values > 11.50:
                            if num_void_suits <= 0.50:
                                if num_nt_kings <= 1.50:
                                    if sum_spades_values <= 13.50:
                                        return 1.0
                                    if sum_spades_values > 13.50:
                                        return 2.0
                                if num_nt_kings > 1.50:
                                    if num_nt_kings <= 2.50:
                                        return 2.0
                                    if num_nt_kings > 2.50:
                                        if sum_spades_values <= 13.50:
                                            return 2.0
                                        if sum_spades_values > 13.50:
                                            return 3.0
                            if num_void_suits > 0.50:
                                if sum_spades_values <= 13.50:
                                    if num_nt_kings <= 1.50:
                                        return 1.0
                                    if num_nt_kings > 1.50:
                                        return 2.0
                                if sum_spades_values > 13.50:
                                    return 1.0
                    if num_nt_aces > 0.50:
                        if num_void_suits <= 0.50:
                            if sum_spades_values <= 10.50:
                                if num_spades <= 0.50:
                                    return 2.0
                                if num_spades > 0.50:
                                    if num_nt_kings <= 0.50:
                                        return 1.0
                                    if num_nt_kings > 0.50:
                                        if num_nt_kings <= 2.50:
                                            return 2.0
                                        if num_nt_kings > 2.50:
                                            return 3.0
                            if sum_spades_values > 10.50:
                                if num_nt_kings <= 2.50:
                                    if sum_spades_values <= 13.50:
                                        return 2.0
                                    if sum_spades_values > 13.50:
                                        if num_nt_kings <= 0.50:
                                            return 2.0
                                        if num_nt_kings > 0.50:
                                            return 3.0
                                if num_nt_kings > 2.50:
                                    if sum_spades_values <= 13.50:
                                        return 3.0
                                    if sum_spades_values > 13.50:
                                        return 4.0
                        if num_void_suits > 0.50:
                            if sum_spades_values <= 13.50:
                                return 2.0
                            if sum_spades_values > 13.50:
                                if num_nt_kings <= 1.50:
                                    return 2.0
                                if num_nt_kings > 1.50:
                                    return 3.0
                if num_spades > 1.50:
                    if sum_spades_values <= 20.50:
                        if num_nt_aces <= 0.50:
                            if sum_spades_values <= 12.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 5.50:
                                        return 2.0
                                    if sum_spades_values > 5.50:
                                        if num_nt_kings <= 0.50:
                                            return 1.0
                                        if num_nt_kings > 0.50:
                                            if num_nt_kings <= 1.50:
                                                if sum_spades_values <= 9.50:
                                                    return 1.0
                                                if sum_spades_values > 9.50:
                                                    if num_spades <= 2.50:
                                                        return 1.0
                                                    if num_spades > 2.50:
                                                        return 2.0
                                            if num_nt_kings > 1.50:
                                                return 2.0
                                if num_void_suits > 0.50:
                                    if num_spades <= 2.50:
                                        if num_nt_kings <= 1.50:
                                            return 2.0
                                        if num_nt_kings > 1.50:
                                            return 3.0
                                    if num_spades > 2.50:
                                        if sum_spades_values <= 11.50:
                                            if sum_spades_values <= 10.50:
                                                if num_nt_kings <= 0.50:
                                                    return 2.0
                                                if num_nt_kings > 0.50:
                                                    return 3.0
                                            if sum_spades_values > 10.50:
                                                return 3.0
                                        if sum_spades_values > 11.50:
                                            return 2.0
                            if sum_spades_values > 12.50:
                                if num_spades <= 2.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 15.50:
                                            if sum_spades_values <= 13.50:
                                                if num_nt_kings <= 1.00:
                                                    return 1.0
                                                if num_nt_kings > 1.00:
                                                    if num_nt_kings <= 2.50:
                                                        return 2.0
                                                    if num_nt_kings > 2.50:
                                                        return 3.0
                                            if sum_spades_values > 13.50:
                                                return 1.0
                                        if sum_spades_values > 15.50:
                                            if num_nt_kings <= 0.50:
                                                return 1.0
                                            if num_nt_kings > 0.50:
                                                if num_nt_kings <= 2.50:
                                                    return 2.0
                                                if num_nt_kings > 2.50:
                                                    return 3.0
                                    if num_void_suits > 0.50:
                                        if num_nt_kings <= 1.50:
                                            return 2.0
                                        if num_nt_kings > 1.50:
                                            return 3.0
                                if num_spades > 2.50:
                                    if num_spades <= 3.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 17.50:
                                                if sum_spades_values <= 16.00:
                                                    if num_void_suits <= 0.50:
                                                        return 1.0
                                                    if num_void_suits > 0.50:
                                                        if num_void_suits <= 1.50:
                                                            return 2.0
                                                        if num_void_suits > 1.50:
                                                            return 3.0
                                                if sum_spades_values > 16.00:
                                                    return 1.0
                                            if sum_spades_values > 17.50:
                                                return 3.0
                                        if num_nt_kings > 0.50:
                                            if sum_spades_values <= 18.50:
                                                if num_void_suits <= 0.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 2.0
                                                    if num_nt_kings > 2.50:
                                                        return 3.0
                                                if num_void_suits > 0.50:
                                                    return 3.0
                                            if sum_spades_values > 18.50:
                                                return 3.0
                                    if num_spades > 3.50:
                                        if num_void_suits <= 0.50:
                                            if num_nt_kings <= 1.50:
                                                if num_nt_kings <= 0.50:
                                                    if num_spades <= 4.50:
                                                        if sum_spades_values <= 14.50:
                                                            return 1.0
                                                        if sum_spades_values > 14.50:
                                                            return 2.0
                                                    if num_spades > 4.50:
                                                        return 2.0
                                                if num_nt_kings > 0.50:
                                                    if num_spades <= 4.50:
                                                        return 2.0
                                                    if num_spades > 4.50:
                                                        return 3.0
                                            if num_nt_kings > 1.50:
                                                if num_nt_kings <= 2.50:
                                                    return 3.0
                                                if num_nt_kings > 2.50:
                                                    if sum_spades_values <= 18.50:
                                                        return 3.0
                                                    if sum_spades_values > 18.50:
                                                        return 4.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 15.50:
                                                if num_void_suits <= 1.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 3.0
                                                    if num_nt_kings > 1.50:
                                                        return 4.0
                                                if num_void_suits > 1.50:
                                                    return 1.0
                                            if sum_spades_values > 15.50:
                                                if num_nt_kings <= 1.50:
                                                    if num_void_suits <= 1.50:
                                                        if sum_spades_values <= 19.00:
                                                            return 3.0
                                                        if sum_spades_values > 19.00:
                                                            if num_nt_kings <= 0.50:
                                                                return 3.0
                                                            if num_nt_kings > 0.50:
                                                                return 4.0
                                                    if num_void_suits > 1.50:
                                                        if num_nt_kings <= 0.50:
                                                            return 2.0
                                                        if num_nt_kings > 0.50:
                                                            if sum_spades_values <= 16.50:
                                                                return 4.0
                                                            if sum_spades_values > 16.50:
                                                                return 3.0
                                                if num_nt_kings > 1.50:
                                                    return 4.0
                        if num_nt_aces > 0.50:
                            if num_nt_kings <= 2.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 10.50:
                                        if num_nt_kings <= 1.50:
                                            if sum_spades_values <= 9.50:
                                                return 2.0
                                            if sum_spades_values > 9.50:
                                                if num_spades <= 2.50:
                                                    return 2.0
                                                if num_spades > 2.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 2.0
                                                    if num_nt_kings > 0.50:
                                                        return 3.0
                                        if num_nt_kings > 1.50:
                                            return 3.0
                                    if sum_spades_values > 10.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 18.50:
                                                if num_spades <= 3.50:
                                                    return 2.0
                                                if num_spades > 3.50:
                                                    return 3.0
                                            if sum_spades_values > 18.50:
                                                if sum_spades_values <= 19.50:
                                                    if num_spades <= 3.50:
                                                        return 2.0
                                                    if num_spades > 3.50:
                                                        return 3.0
                                                if sum_spades_values > 19.50:
                                                    if num_spades <= 4.00:
                                                        return 2.0
                                                    if num_spades > 4.00:
                                                        return 3.0
                                        if num_nt_kings > 0.50:
                                            if sum_spades_values <= 15.50:
                                                if num_spades <= 2.50:
                                                    if sum_spades_values <= 12.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 2.0
                                                        if num_nt_kings > 1.50:
                                                            return 3.0
                                                    if sum_spades_values > 12.50:
                                                        if sum_spades_values <= 13.50:
                                                            if num_nt_kings <= 1.50:
                                                                return 2.0
                                                            if num_nt_kings > 1.50:
                                                                return 3.0
                                                        if sum_spades_values > 13.50:
                                                            if sum_spades_values <= 14.50:
                                                                if num_nt_kings <= 1.50:
                                                                    return 2.0
                                                                if num_nt_kings > 1.50:
                                                                    return 3.0
                                                            if sum_spades_values > 14.50:
                                                                if num_nt_kings <= 1.50:
                                                                    return 2.0
                                                                if num_nt_kings > 1.50:
                                                                    return 3.0
                                                if num_spades > 2.50:
                                                    if num_spades <= 3.50:
                                                        return 3.0
                                                    if num_spades > 3.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 3.0
                                                        if num_nt_kings > 1.50:
                                                            return 4.0
                                            if sum_spades_values > 15.50:
                                                if num_nt_kings <= 1.50:
                                                    if num_spades <= 4.50:
                                                        return 3.0
                                                    if num_spades > 4.50:
                                                        return 4.0
                                                if num_nt_kings > 1.50:
                                                    if num_spades <= 3.50:
                                                        if num_spades <= 2.50:
                                                            return 3.0
                                                        if num_spades > 2.50:
                                                            if sum_spades_values <= 18.50:
                                                                return 3.0
                                                            if sum_spades_values > 18.50:
                                                                return 4.0
                                                    if num_spades > 3.50:
                                                        return 4.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 10.50:
                                        if num_spades <= 2.50:
                                            return 3.0
                                        if num_spades > 2.50:
                                            if sum_spades_values <= 9.50:
                                                if num_void_suits <= 1.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 3.0
                                                    if num_nt_kings > 0.50:
                                                        return 4.0
                                                if num_void_suits > 1.50:
                                                    return 3.0
                                            if sum_spades_values > 9.50:
                                                if num_void_suits <= 1.50:
                                                    if num_nt_kings <= 1.00:
                                                        return 3.0
                                                    if num_nt_kings > 1.00:
                                                        return 4.0
                                                if num_void_suits > 1.50:
                                                    return 3.0
                                    if sum_spades_values > 10.50:
                                        if num_spades <= 2.50:
                                            if num_nt_kings <= 1.50:
                                                if sum_spades_values <= 14.50:
                                                    return 3.0
                                                if sum_spades_values > 14.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 3.0
                                                    if num_nt_kings > 0.50:
                                                        if sum_spades_values <= 15.50:
                                                            return 2.0
                                                        if sum_spades_values > 15.50:
                                                            if num_void_suits <= 1.50:
                                                                return 3.0
                                                            if num_void_suits > 1.50:
                                                                return 2.0
                                            if num_nt_kings > 1.50:
                                                return 3.0
                                        if num_spades > 2.50:
                                            if num_spades <= 3.50:
                                                if num_void_suits <= 1.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 3.0
                                                    if num_nt_kings > 0.50:
                                                        return 4.0
                                                if num_void_suits > 1.50:
                                                    if sum_spades_values <= 16.50:
                                                        if sum_spades_values <= 12.50:
                                                            if num_nt_kings <= 0.50:
                                                                return 1.0
                                                            if num_nt_kings > 0.50:
                                                                return 2.0
                                                        if sum_spades_values > 12.50:
                                                            if num_nt_kings <= 0.50:
                                                                return 2.0
                                                            if num_nt_kings > 0.50:
                                                                return 3.0
                                                    if sum_spades_values > 16.50:
                                                        if sum_spades_values <= 19.00:
                                                            return 3.0
                                                        if sum_spades_values > 19.00:
                                                            return 4.0
                                            if num_spades > 3.50:
                                                if num_spades <= 4.50:
                                                    if num_void_suits <= 1.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 4.0
                                                        if num_nt_kings > 1.50:
                                                            return 5.0
                                                    if num_void_suits > 1.50:
                                                        if sum_spades_values <= 16.50:
                                                            if num_nt_kings <= 0.50:
                                                                return 4.0
                                                            if num_nt_kings > 0.50:
                                                                if sum_spades_values <= 14.50:
                                                                    return 4.0
                                                                if sum_spades_values > 14.50:
                                                                    if sum_spades_values <= 15.50:
                                                                        return 2.0
                                                                    if sum_spades_values > 15.50:
                                                                        return 3.0
                                                        if sum_spades_values > 16.50:
                                                            if sum_spades_values <= 19.50:
                                                                if sum_spades_values <= 18.00:
                                                                    if num_nt_kings <= 0.50:
                                                                        return 4.0
                                                                    if num_nt_kings > 0.50:
                                                                        return 5.0
                                                                if sum_spades_values > 18.00:
                                                                    return 5.0
                                                            if sum_spades_values > 19.50:
                                                                return 4.0
                                                if num_spades > 4.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_void_suits <= 1.50:
                                                            return 5.0
                                                        if num_void_suits > 1.50:
                                                            return 7.0
                                                    if num_nt_kings > 1.50:
                                                        return 6.0
                            if num_nt_kings > 2.50:
                                if sum_spades_values <= 14.00:
                                    if num_spades <= 2.50:
                                        return 3.0
                                    if num_spades > 2.50:
                                        return 4.0
                                if sum_spades_values > 14.00:
                                    if sum_spades_values <= 19.50:
                                        return 4.0
                                    if sum_spades_values > 19.50:
                                        return 5.0
                    if sum_spades_values > 20.50:
                        if num_spades <= 3.50:
                            if num_nt_aces <= 0.50:
                                if num_spades <= 2.50:
                                    if num_nt_kings <= 1.50:
                                        return 2.0
                                    if num_nt_kings > 1.50:
                                        if num_void_suits <= 0.50:
                                            if sum_spades_values <= 22.00:
                                                return 2.0
                                            if sum_spades_values > 22.00:
                                                return 3.0
                                        if num_void_suits > 0.50:
                                            return 3.0
                                if num_spades > 2.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 21.50:
                                            if num_nt_kings <= 0.50:
                                                return 1.0
                                            if num_nt_kings > 0.50:
                                                if num_nt_kings <= 2.00:
                                                    return 2.0
                                                if num_nt_kings > 2.00:
                                                    return 3.0
                                        if sum_spades_values > 21.50:
                                            if num_nt_kings <= 1.50:
                                                return 2.0
                                            if num_nt_kings > 1.50:
                                                return 3.0
                                    if num_void_suits > 0.50:
                                        if num_nt_kings <= 1.50:
                                            return 3.0
                                        if num_nt_kings > 1.50:
                                            return 4.0
                            if num_nt_aces > 0.50:
                                if sum_spades_values <= 21.50:
                                    if num_void_suits <= 0.50:
                                        if num_spades <= 2.50:
                                            if num_nt_kings <= 2.50:
                                                if num_nt_kings <= 1.00:
                                                    return 2.0
                                                if num_nt_kings > 1.00:
                                                    return 3.0
                                            if num_nt_kings > 2.50:
                                                return 4.0
                                        if num_spades > 2.50:
                                            if num_nt_kings <= 1.50:
                                                return 3.0
                                            if num_nt_kings > 1.50:
                                                return 4.0
                                    if num_void_suits > 0.50:
                                        if num_spades <= 2.50:
                                            if num_void_suits <= 1.50:
                                                return 3.0
                                            if num_void_suits > 1.50:
                                                return 2.0
                                        if num_spades > 2.50:
                                            return 3.0
                                if sum_spades_values > 21.50:
                                    if num_nt_kings <= 1.50:
                                        if num_nt_kings <= 0.50:
                                            if num_void_suits <= 0.50:
                                                if sum_spades_values <= 23.50:
                                                    return 2.0
                                                if sum_spades_values > 23.50:
                                                    return 3.0
                                            if num_void_suits > 0.50:
                                                if sum_spades_values <= 23.50:
                                                    if num_spades <= 2.50:
                                                        return 3.0
                                                    if num_spades > 2.50:
                                                        return 4.0
                                                if sum_spades_values > 23.50:
                                                    if num_spades <= 2.50:
                                                        return 3.0
                                                    if num_spades > 2.50:
                                                        return 4.0
                                        if num_nt_kings > 0.50:
                                            if num_spades <= 2.50:
                                                return 3.0
                                            if num_spades > 2.50:
                                                if num_void_suits <= 1.50:
                                                    if sum_spades_values <= 22.50:
                                                        return 4.0
                                                    if sum_spades_values > 22.50:
                                                        if num_void_suits <= 0.50:
                                                            return 3.0
                                                        if num_void_suits > 0.50:
                                                            return 4.0
                                                if num_void_suits > 1.50:
                                                    return 3.0
                                    if num_nt_kings > 1.50:
                                        if num_spades <= 2.50:
                                            if sum_spades_values <= 23.50:
                                                if num_void_suits <= 0.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 3.0
                                                    if num_nt_kings > 2.50:
                                                        return 4.0
                                                if num_void_suits > 0.50:
                                                    return 4.0
                                            if sum_spades_values > 23.50:
                                                return 4.0
                                        if num_spades > 2.50:
                                            return 4.0
                        if num_spades > 3.50:
                            if num_nt_aces <= 0.50:
                                if sum_spades_values <= 22.50:
                                    if num_void_suits <= 0.50:
                                        if num_spades <= 4.50:
                                            if sum_spades_values <= 21.50:
                                                if num_nt_kings <= 2.00:
                                                    return 2.0
                                                if num_nt_kings > 2.00:
                                                    return 4.0
                                            if sum_spades_values > 21.50:
                                                return 3.0
                                        if num_spades > 4.50:
                                            if num_nt_kings <= 0.50:
                                                return 2.0
                                            if num_nt_kings > 0.50:
                                                if sum_spades_values <= 21.50:
                                                    return 4.0
                                                if sum_spades_values > 21.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 3.0
                                                    if num_nt_kings > 1.50:
                                                        return 4.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 21.50:
                                            if num_spades <= 4.50:
                                                if num_nt_kings <= 0.50:
                                                    return 3.0
                                                if num_nt_kings > 0.50:
                                                    return 4.0
                                            if num_spades > 4.50:
                                                if num_nt_kings <= 1.00:
                                                    return 4.0
                                                if num_nt_kings > 1.00:
                                                    return 5.0
                                        if sum_spades_values > 21.50:
                                            if num_nt_kings <= 0.50:
                                                return 3.0
                                            if num_nt_kings > 0.50:
                                                if num_spades <= 4.50:
                                                    return 4.0
                                                if num_spades > 4.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 4.0
                                                    if num_nt_kings > 1.50:
                                                        return 5.0
                                if sum_spades_values > 22.50:
                                    if num_void_suits <= 1.50:
                                        if num_void_suits <= 0.50:
                                            if num_nt_kings <= 1.50:
                                                if num_nt_kings <= 0.50:
                                                    return 2.0
                                                if num_nt_kings > 0.50:
                                                    return 3.0
                                            if num_nt_kings > 1.50:
                                                if sum_spades_values <= 23.50:
                                                    return 4.0
                                                if sum_spades_values > 23.50:
                                                    if num_spades <= 4.50:
                                                        if num_nt_kings <= 2.50:
                                                            return 3.0
                                                        if num_nt_kings > 2.50:
                                                            return 4.0
                                                    if num_spades > 4.50:
                                                        return 4.0
                                        if num_void_suits > 0.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 23.50:
                                                    return 4.0
                                                if sum_spades_values > 23.50:
                                                    if num_spades <= 4.50:
                                                        return 3.0
                                                    if num_spades > 4.50:
                                                        return 4.0
                                            if num_nt_kings > 0.50:
                                                return 4.0
                                    if num_void_suits > 1.50:
                                        if num_spades <= 4.50:
                                            if sum_spades_values <= 23.50:
                                                return 4.0
                                            if sum_spades_values > 23.50:
                                                return 3.0
                                        if num_spades > 4.50:
                                            return 4.0
                            if num_nt_aces > 0.50:
                                if num_nt_kings <= 0.50:
                                    if num_spades <= 4.50:
                                        if num_void_suits <= 0.50:
                                            return 3.0
                                        if num_void_suits > 0.50:
                                            if num_void_suits <= 1.50:
                                                return 4.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 21.50:
                                                    return 4.0
                                                if sum_spades_values > 21.50:
                                                    if sum_spades_values <= 22.50:
                                                        return 5.0
                                                    if sum_spades_values > 22.50:
                                                        return 4.0
                                    if num_spades > 4.50:
                                        if num_void_suits <= 0.50:
                                            return 3.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 21.50:
                                                return 8.0
                                            if sum_spades_values > 21.50:
                                                if num_void_suits <= 1.50:
                                                    return 5.0
                                                if num_void_suits > 1.50:
                                                    return 7.0
                                if num_nt_kings > 0.50:
                                    if num_nt_kings <= 2.50:
                                        if sum_spades_values <= 22.50:
                                            if num_void_suits <= 1.50:
                                                if num_spades <= 4.50:
                                                    if num_void_suits <= 0.50:
                                                        return 4.0
                                                    if num_void_suits > 0.50:
                                                        if num_nt_kings <= 1.50:
                                                            if sum_spades_values <= 21.50:
                                                                return 4.0
                                                            if sum_spades_values > 21.50:
                                                                return 5.0
                                                        if num_nt_kings > 1.50:
                                                            return 5.0
                                                if num_spades > 4.50:
                                                    if sum_spades_values <= 21.50:
                                                        return 5.0
                                                    if sum_spades_values > 21.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 5.0
                                                        if num_nt_kings > 1.50:
                                                            return 6.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 21.50:
                                                    return 7.0
                                                if sum_spades_values > 21.50:
                                                    return 5.0
                                        if sum_spades_values > 22.50:
                                            if num_spades <= 4.50:
                                                if num_void_suits <= 0.50:
                                                    return 4.0
                                                if num_void_suits > 0.50:
                                                    if num_void_suits <= 1.50:
                                                        return 5.0
                                                    if num_void_suits > 1.50:
                                                        if sum_spades_values <= 23.50:
                                                            return 3.0
                                                        if sum_spades_values > 23.50:
                                                            return 4.0
                                            if num_spades > 4.50:
                                                if num_nt_kings <= 1.50:
                                                    if num_void_suits <= 0.50:
                                                        return 4.0
                                                    if num_void_suits > 0.50:
                                                        return 5.0
                                                if num_nt_kings > 1.50:
                                                    return 6.0
                                    if num_nt_kings > 2.50:
                                        return 5.0
            if num_nt_aces > 1.50:
                if num_nt_kings <= 0.50:
                    if num_spades <= 1.50:
                        if sum_spades_values <= 12.50:
                            if sum_spades_values <= 11.50:
                                if sum_spades_values <= 3.00:
                                    if num_nt_aces <= 2.50:
                                        if num_void_suits <= 0.50:
                                            return 2.0
                                        if num_void_suits > 0.50:
                                            return 3.0
                                    if num_nt_aces > 2.50:
                                        return 3.0
                                if sum_spades_values > 3.00:
                                    if num_void_suits <= 0.50:
                                        if num_nt_aces <= 2.50:
                                            return 2.0
                                        if num_nt_aces > 2.50:
                                            return 3.0
                                    if num_void_suits > 0.50:
                                        return 3.0
                            if sum_spades_values > 11.50:
                                return 3.0
                        if sum_spades_values > 12.50:
                            if num_void_suits <= 0.50:
                                return 4.0
                            if num_void_suits > 0.50:
                                return 3.0
                    if num_spades > 1.50:
                        if num_spades <= 3.50:
                            if sum_spades_values <= 5.50:
                                return 3.0
                            if sum_spades_values > 5.50:
                                if sum_spades_values <= 21.50:
                                    if num_nt_aces <= 2.50:
                                        if sum_spades_values <= 19.50:
                                            if num_void_suits <= 0.50:
                                                return 3.0
                                            if num_void_suits > 0.50:
                                                return 4.0
                                        if sum_spades_values > 19.50:
                                            if num_void_suits <= 0.50:
                                                return 3.0
                                            if num_void_suits > 0.50:
                                                return 4.0
                                    if num_nt_aces > 2.50:
                                        return 4.0
                                if sum_spades_values > 21.50:
                                    if num_spades <= 2.50:
                                        return 4.0
                                    if num_spades > 2.50:
                                        if sum_spades_values <= 22.50:
                                            return 4.0
                                        if sum_spades_values > 22.50:
                                            if sum_spades_values <= 23.50:
                                                if num_nt_aces <= 2.50:
                                                    return 4.0
                                                if num_nt_aces > 2.50:
                                                    return 5.0
                                            if sum_spades_values > 23.50:
                                                return 4.0
                        if num_spades > 3.50:
                            if sum_spades_values <= 18.50:
                                if sum_spades_values <= 15.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_aces <= 2.50:
                                            return 3.0
                                        if num_nt_aces > 2.50:
                                            return 4.0
                                    if num_void_suits > 0.50:
                                        return 5.0
                                if sum_spades_values > 15.50:
                                    return 4.0
                            if sum_spades_values > 18.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 19.50:
                                        return 5.0
                                    if sum_spades_values > 19.50:
                                        if sum_spades_values <= 22.50:
                                            if sum_spades_values <= 21.50:
                                                if num_spades <= 4.50:
                                                    if num_nt_aces <= 2.50:
                                                        return 4.0
                                                    if num_nt_aces > 2.50:
                                                        return 5.0
                                                if num_spades > 4.50:
                                                    if sum_spades_values <= 20.50:
                                                        return 4.0
                                                    if sum_spades_values > 20.50:
                                                        if num_nt_aces <= 2.50:
                                                            return 4.0
                                                        if num_nt_aces > 2.50:
                                                            return 5.0
                                            if sum_spades_values > 21.50:
                                                return 4.0
                                        if sum_spades_values > 22.50:
                                            return 5.0
                                if num_void_suits > 0.50:
                                    return 5.0
                if num_nt_kings > 0.50:
                    if num_spades <= 2.50:
                        if num_nt_aces <= 2.50:
                            if num_void_suits <= 0.50:
                                if num_nt_kings <= 2.50:
                                    if sum_spades_values <= 12.50:
                                        if sum_spades_values <= 5.50:
                                            return 3.0
                                        if sum_spades_values > 5.50:
                                            if sum_spades_values <= 6.50:
                                                if num_nt_kings <= 1.50:
                                                    return 3.0
                                                if num_nt_kings > 1.50:
                                                    if num_spades <= 1.50:
                                                        return 3.0
                                                    if num_spades > 1.50:
                                                        return 4.0
                                            if sum_spades_values > 6.50:
                                                if num_nt_kings <= 1.50:
                                                    return 3.0
                                                if num_nt_kings > 1.50:
                                                    if sum_spades_values <= 11.50:
                                                        if num_spades <= 1.50:
                                                            return 3.0
                                                        if num_spades > 1.50:
                                                            return 4.0
                                                    if sum_spades_values > 11.50:
                                                        return 3.0
                                    if sum_spades_values > 12.50:
                                        if sum_spades_values <= 23.00:
                                            if sum_spades_values <= 15.00:
                                                if sum_spades_values <= 13.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 3.0
                                                    if num_nt_kings > 1.50:
                                                        return 4.0
                                                if sum_spades_values > 13.50:
                                                    if num_spades <= 1.50:
                                                        return 4.0
                                                    if num_spades > 1.50:
                                                        return 3.0
                                            if sum_spades_values > 15.00:
                                                return 4.0
                                        if sum_spades_values > 23.00:
                                            if num_nt_kings <= 1.50:
                                                return 4.0
                                            if num_nt_kings > 1.50:
                                                return 5.0
                                if num_nt_kings > 2.50:
                                    if num_spades <= 1.50:
                                        if sum_spades_values <= 13.00:
                                            return 4.0
                                        if sum_spades_values > 13.00:
                                            return 5.0
                                    if num_spades > 1.50:
                                        if sum_spades_values <= 13.00:
                                            return 4.0
                                        if sum_spades_values > 13.00:
                                            return 5.0
                            if num_void_suits > 0.50:
                                if num_spades <= 1.50:
                                    if num_nt_kings <= 1.50:
                                        if sum_spades_values <= 1.00:
                                            return 2.0
                                        if sum_spades_values > 1.00:
                                            return 3.0
                                    if num_nt_kings > 1.50:
                                        if num_spades <= 0.50:
                                            return 2.0
                                        if num_spades > 0.50:
                                            return 3.0
                                if num_spades > 1.50:
                                    return 4.0
                        if num_nt_aces > 2.50:
                            if num_nt_kings <= 1.50:
                                if sum_spades_values <= 15.00:
                                    if sum_spades_values <= 13.00:
                                        return 4.0
                                    if sum_spades_values > 13.00:
                                        if num_spades <= 1.50:
                                            return 5.0
                                        if num_spades > 1.50:
                                            return 4.0
                                if sum_spades_values > 15.00:
                                    return 5.0
                            if num_nt_kings > 1.50:
                                if num_spades <= 1.50:
                                    if sum_spades_values <= 11.50:
                                        if sum_spades_values <= 1.50:
                                            if num_nt_kings <= 2.50:
                                                return 4.0
                                            if num_nt_kings > 2.50:
                                                return 5.0
                                        if sum_spades_values > 1.50:
                                            if sum_spades_values <= 4.50:
                                                return 4.0
                                            if sum_spades_values > 4.50:
                                                if sum_spades_values <= 6.50:
                                                    return 5.0
                                                if sum_spades_values > 6.50:
                                                    if sum_spades_values <= 8.50:
                                                        if num_nt_kings <= 2.50:
                                                            return 4.0
                                                        if num_nt_kings > 2.50:
                                                            return 5.0
                                                    if sum_spades_values > 8.50:
                                                        if sum_spades_values <= 10.00:
                                                            return 5.0
                                                        if sum_spades_values > 10.00:
                                                            if num_nt_kings <= 2.50:
                                                                return 4.0
                                                            if num_nt_kings > 2.50:
                                                                return 5.0
                                    if sum_spades_values > 11.50:
                                        if sum_spades_values <= 13.50:
                                            return 5.0
                                        if sum_spades_values > 13.50:
                                            if num_nt_kings <= 2.50:
                                                return 5.0
                                            if num_nt_kings > 2.50:
                                                return 6.0
                                if num_spades > 1.50:
                                    if sum_spades_values <= 21.00:
                                        if sum_spades_values <= 17.00:
                                            if num_nt_kings <= 2.50:
                                                return 5.0
                                            if num_nt_kings > 2.50:
                                                if sum_spades_values <= 13.00:
                                                    return 5.0
                                                if sum_spades_values > 13.00:
                                                    return 6.0
                                        if sum_spades_values > 17.00:
                                            if sum_spades_values <= 18.50:
                                                if num_nt_kings <= 2.50:
                                                    return 5.0
                                                if num_nt_kings > 2.50:
                                                    return 6.0
                                            if sum_spades_values > 18.50:
                                                if num_nt_kings <= 2.50:
                                                    return 5.0
                                                if num_nt_kings > 2.50:
                                                    return 6.0
                                    if sum_spades_values > 21.00:
                                        return 6.0
                    if num_spades > 2.50:
                        if num_spades <= 4.50:
                            if num_nt_aces <= 2.50:
                                if num_spades <= 3.50:
                                    if sum_spades_values <= 12.50:
                                        if sum_spades_values <= 10.50:
                                            if num_nt_kings <= 2.50:
                                                if sum_spades_values <= 9.50:
                                                    return 4.0
                                                if sum_spades_values > 9.50:
                                                    if num_void_suits <= 0.50:
                                                        return 4.0
                                                    if num_void_suits > 0.50:
                                                        return 5.0
                                            if num_nt_kings > 2.50:
                                                return 5.0
                                        if sum_spades_values > 10.50:
                                            if num_nt_kings <= 1.50:
                                                if num_void_suits <= 0.50:
                                                    return 4.0
                                                if num_void_suits > 0.50:
                                                    return 5.0
                                            if num_nt_kings > 1.50:
                                                if sum_spades_values <= 11.50:
                                                    if num_void_suits <= 0.50:
                                                        return 4.0
                                                    if num_void_suits > 0.50:
                                                        return 5.0
                                                if sum_spades_values > 11.50:
                                                    return 4.0
                                    if sum_spades_values > 12.50:
                                        if sum_spades_values <= 18.50:
                                            if num_nt_kings <= 1.50:
                                                if num_void_suits <= 0.50:
                                                    return 4.0
                                                if num_void_suits > 0.50:
                                                    return 5.0
                                            if num_nt_kings > 1.50:
                                                if num_void_suits <= 0.50:
                                                    if sum_spades_values <= 15.50:
                                                        return 4.0
                                                    if sum_spades_values > 15.50:
                                                        return 5.0
                                                if num_void_suits > 0.50:
                                                    return 5.0
                                        if sum_spades_values > 18.50:
                                            if sum_spades_values <= 22.50:
                                                if num_void_suits <= 0.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 4.0
                                                    if num_nt_kings > 1.50:
                                                        return 5.0
                                                if num_void_suits > 0.50:
                                                    return 5.0
                                            if sum_spades_values > 22.50:
                                                if sum_spades_values <= 23.50:
                                                    if num_nt_kings <= 2.00:
                                                        return 4.0
                                                    if num_nt_kings > 2.00:
                                                        return 5.0
                                                if sum_spades_values > 23.50:
                                                    return 5.0
                                if num_spades > 3.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 21.50:
                                            if num_nt_kings <= 1.50:
                                                return 4.0
                                            if num_nt_kings > 1.50:
                                                return 5.0
                                        if sum_spades_values > 21.50:
                                            if num_nt_kings <= 2.50:
                                                return 5.0
                                            if num_nt_kings > 2.50:
                                                return 6.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 15.50:
                                            return 5.0
                                        if sum_spades_values > 15.50:
                                            if num_nt_kings <= 1.50:
                                                if sum_spades_values <= 21.00:
                                                    return 5.0
                                                if sum_spades_values > 21.00:
                                                    return 6.0
                                            if num_nt_kings > 1.50:
                                                return 6.0
                            if num_nt_aces > 2.50:
                                if num_nt_kings <= 1.50:
                                    if num_spades <= 3.50:
                                        return 5.0
                                    if num_spades > 3.50:
                                        if sum_spades_values <= 22.00:
                                            return 5.0
                                        if sum_spades_values > 22.00:
                                            return 6.0
                                if num_nt_kings > 1.50:
                                    if num_spades <= 3.50:
                                        if sum_spades_values <= 10.50:
                                            return 5.0
                                        if sum_spades_values > 10.50:
                                            if sum_spades_values <= 23.50:
                                                if sum_spades_values <= 13.00:
                                                    if num_nt_kings <= 2.50:
                                                        return 5.0
                                                    if num_nt_kings > 2.50:
                                                        return 6.0
                                                if sum_spades_values > 13.00:
                                                    return 6.0
                                            if sum_spades_values > 23.50:
                                                return 7.0
                                    if num_spades > 3.50:
                                        if sum_spades_values <= 18.50:
                                            return 6.0
                                        if sum_spades_values > 18.50:
                                            if sum_spades_values <= 19.50:
                                                if num_nt_kings <= 2.50:
                                                    return 6.0
                                                if num_nt_kings > 2.50:
                                                    return 7.0
                                            if sum_spades_values > 19.50:
                                                if sum_spades_values <= 20.50:
                                                    return 6.0
                                                if sum_spades_values > 20.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 6.0
                                                    if num_nt_kings > 2.50:
                                                        return 7.0
                        if num_spades > 4.50:
                            if sum_spades_values <= 23.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 22.50:
                                        if sum_spades_values <= 20.50:
                                            return 6.0
                                        if sum_spades_values > 20.50:
                                            if sum_spades_values <= 21.50:
                                                if num_nt_aces <= 2.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 5.0
                                                    if num_nt_kings > 2.50:
                                                        return 6.0
                                                if num_nt_aces > 2.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 6.0
                                                    if num_nt_kings > 2.50:
                                                        return 7.0
                                            if sum_spades_values > 21.50:
                                                if num_nt_kings <= 2.00:
                                                    return 5.0
                                                if num_nt_kings > 2.00:
                                                    return 6.0
                                    if sum_spades_values > 22.50:
                                        if num_nt_aces <= 2.50:
                                            return 6.0
                                        if num_nt_aces > 2.50:
                                            if num_nt_kings <= 2.00:
                                                return 6.0
                                            if num_nt_kings > 2.00:
                                                return 7.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 21.00:
                                        if num_nt_kings <= 1.50:
                                            return 6.0
                                        if num_nt_kings > 1.50:
                                            return 7.0
                                    if sum_spades_values > 21.00:
                                        if num_nt_kings <= 1.50:
                                            return 6.0
                                        if num_nt_kings > 1.50:
                                            return 7.0
                            if sum_spades_values > 23.50:
                                if num_nt_aces <= 2.50:
                                    if num_nt_kings <= 1.50:
                                        if num_void_suits <= 0.50:
                                            return 5.0
                                        if num_void_suits > 0.50:
                                            return 6.0
                                    if num_nt_kings > 1.50:
                                        if num_void_suits <= 0.50:
                                            return 6.0
                                        if num_void_suits > 0.50:
                                            return 7.0
                                if num_nt_aces > 2.50:
                                    return 7.0
        if sum_spades_values > 24.50:
            if num_nt_aces <= 1.50:
                if num_spades <= 4.50:
                    if sum_spades_values <= 38.50:
                        if num_nt_kings <= 1.50:
                            if num_nt_aces <= 0.50:
                                if sum_spades_values <= 36.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 32.50:
                                                return 2.0
                                            if sum_spades_values > 32.50:
                                                if num_spades <= 3.50:
                                                    return 2.0
                                                if num_spades > 3.50:
                                                    return 3.0
                                        if num_nt_kings > 0.50:
                                            if num_spades <= 3.50:
                                                if sum_spades_values <= 27.00:
                                                    return 2.0
                                                if sum_spades_values > 27.00:
                                                    return 3.0
                                            if num_spades > 3.50:
                                                return 3.0
                                    if num_void_suits > 0.50:
                                        if num_void_suits <= 1.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 31.50:
                                                    return 3.0
                                                if sum_spades_values > 31.50:
                                                    if sum_spades_values <= 34.50:
                                                        return 4.0
                                                    if sum_spades_values > 34.50:
                                                        return 3.0
                                            if num_nt_kings > 0.50:
                                                if num_spades <= 3.50:
                                                    return 3.0
                                                if num_spades > 3.50:
                                                    return 4.0
                                        if num_void_suits > 1.50:
                                            if sum_spades_values <= 33.50:
                                                if num_spades <= 3.50:
                                                    return 3.0
                                                if num_spades > 3.50:
                                                    if sum_spades_values <= 32.50:
                                                        return 4.0
                                                    if sum_spades_values > 32.50:
                                                        if num_nt_kings <= 0.50:
                                                            return 3.0
                                                        if num_nt_kings > 0.50:
                                                            return 4.0
                                            if sum_spades_values > 33.50:
                                                return 4.0
                                if sum_spades_values > 36.50:
                                    if num_spades <= 3.50:
                                        if num_void_suits <= 0.50:
                                            if num_nt_kings <= 0.50:
                                                return 3.0
                                            if num_nt_kings > 0.50:
                                                return 4.0
                                        if num_void_suits > 0.50:
                                            if num_nt_kings <= 0.50:
                                                return 3.0
                                            if num_nt_kings > 0.50:
                                                return 4.0
                                    if num_spades > 3.50:
                                        if num_nt_kings <= 0.50:
                                            if num_void_suits <= 0.50:
                                                return 3.0
                                            if num_void_suits > 0.50:
                                                return 4.0
                                        if num_nt_kings > 0.50:
                                            return 4.0
                            if num_nt_aces > 0.50:
                                if num_spades <= 3.50:
                                    if sum_spades_values <= 32.50:
                                        if num_void_suits <= 1.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 27.50:
                                                    if num_void_suits <= 0.50:
                                                        return 3.0
                                                    if num_void_suits > 0.50:
                                                        if sum_spades_values <= 25.50:
                                                            return 3.0
                                                        if sum_spades_values > 25.50:
                                                            return 4.0
                                                if sum_spades_values > 27.50:
                                                    if num_void_suits <= 0.50:
                                                        return 3.0
                                                    if num_void_suits > 0.50:
                                                        return 4.0
                                            if num_nt_kings > 0.50:
                                                if sum_spades_values <= 27.50:
                                                    if num_void_suits <= 0.50:
                                                        return 3.0
                                                    if num_void_suits > 0.50:
                                                        if num_spades <= 2.50:
                                                            return 3.0
                                                        if num_spades > 2.50:
                                                            return 4.0
                                                if sum_spades_values > 27.50:
                                                    return 4.0
                                        if num_void_suits > 1.50:
                                            if num_spades <= 2.50:
                                                return 2.0
                                            if num_spades > 2.50:
                                                return 3.0
                                    if sum_spades_values > 32.50:
                                        if sum_spades_values <= 37.50:
                                            if num_void_suits <= 1.50:
                                                if sum_spades_values <= 33.50:
                                                    if num_nt_kings <= 0.50:
                                                        if num_void_suits <= 0.50:
                                                            return 3.0
                                                        if num_void_suits > 0.50:
                                                            return 4.0
                                                    if num_nt_kings > 0.50:
                                                        return 4.0
                                                if sum_spades_values > 33.50:
                                                    return 4.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 35.50:
                                                    return 3.0
                                                if sum_spades_values > 35.50:
                                                    return 4.0
                                        if sum_spades_values > 37.50:
                                            return 5.0
                                if num_spades > 3.50:
                                    if num_nt_kings <= 0.50:
                                        if num_void_suits <= 1.50:
                                            if sum_spades_values <= 29.50:
                                                if num_void_suits <= 0.50:
                                                    return 3.0
                                                if num_void_suits > 0.50:
                                                    return 4.0
                                            if sum_spades_values > 29.50:
                                                if sum_spades_values <= 34.50:
                                                    return 4.0
                                                if sum_spades_values > 34.50:
                                                    if num_void_suits <= 0.50:
                                                        return 4.0
                                                    if num_void_suits > 0.50:
                                                        return 5.0
                                        if num_void_suits > 1.50:
                                            return 4.0
                                    if num_nt_kings > 0.50:
                                        if num_void_suits <= 0.50:
                                            if sum_spades_values <= 35.50:
                                                return 4.0
                                            if sum_spades_values > 35.50:
                                                return 5.0
                                        if num_void_suits > 0.50:
                                            if num_void_suits <= 1.50:
                                                return 5.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 36.50:
                                                    return 4.0
                                                if sum_spades_values > 36.50:
                                                    return 5.0
                        if num_nt_kings > 1.50:
                            if num_nt_aces <= 0.50:
                                if num_void_suits <= 0.50:
                                    if num_nt_kings <= 2.50:
                                        if sum_spades_values <= 27.50:
                                            return 3.0
                                        if sum_spades_values > 27.50:
                                            if sum_spades_values <= 31.50:
                                                if sum_spades_values <= 30.00:
                                                    return 4.0
                                                if sum_spades_values > 30.00:
                                                    return 3.0
                                            if sum_spades_values > 31.50:
                                                return 4.0
                                    if num_nt_kings > 2.50:
                                        if num_spades <= 2.50:
                                            return 4.0
                                        if num_spades > 2.50:
                                            if num_spades <= 3.50:
                                                if sum_spades_values <= 35.50:
                                                    return 4.0
                                                if sum_spades_values > 35.50:
                                                    return 5.0
                                            if num_spades > 3.50:
                                                if sum_spades_values <= 33.00:
                                                    return 4.0
                                                if sum_spades_values > 33.00:
                                                    return 5.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 31.00:
                                        return 4.0
                                    if sum_spades_values > 31.00:
                                        if sum_spades_values <= 34.50:
                                            if num_spades <= 3.50:
                                                return 4.0
                                            if num_spades > 3.50:
                                                return 5.0
                                        if sum_spades_values > 34.50:
                                            if sum_spades_values <= 36.00:
                                                return 5.0
                                            if sum_spades_values > 36.00:
                                                if num_spades <= 3.50:
                                                    return 4.0
                                                if num_spades > 3.50:
                                                    return 5.0
                            if num_nt_aces > 0.50:
                                if num_nt_kings <= 2.50:
                                    if num_spades <= 2.50:
                                        return 4.0
                                    if num_spades > 2.50:
                                        if num_void_suits <= 0.50:
                                            if num_spades <= 3.50:
                                                if sum_spades_values <= 33.00:
                                                    return 4.0
                                                if sum_spades_values > 33.00:
                                                    return 5.0
                                            if num_spades > 3.50:
                                                return 5.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 30.00:
                                                return 5.0
                                            if sum_spades_values > 30.00:
                                                if num_spades <= 3.50:
                                                    return 5.0
                                                if num_spades > 3.50:
                                                    return 6.0
                                if num_nt_kings > 2.50:
                                    if sum_spades_values <= 36.00:
                                        if sum_spades_values <= 32.50:
                                            if num_spades <= 2.50:
                                                return 4.0
                                            if num_spades > 2.50:
                                                return 5.0
                                        if sum_spades_values > 32.50:
                                            if num_spades <= 3.50:
                                                return 5.0
                                            if num_spades > 3.50:
                                                return 6.0
                                    if sum_spades_values > 36.00:
                                        return 6.0
                    if sum_spades_values > 38.50:
                        if num_void_suits <= 1.50:
                            if sum_spades_values <= 40.50:
                                if num_void_suits <= 0.50:
                                    if num_nt_kings <= 0.50:
                                        return 4.0
                                    if num_nt_kings > 0.50:
                                        if num_nt_kings <= 2.50:
                                            if num_nt_aces <= 0.50:
                                                return 4.0
                                            if num_nt_aces > 0.50:
                                                return 5.0
                                        if num_nt_kings > 2.50:
                                            return 5.0
                                if num_void_suits > 0.50:
                                    if num_nt_aces <= 0.50:
                                        if num_nt_kings <= 1.50:
                                            return 4.0
                                        if num_nt_kings > 1.50:
                                            return 5.0
                                    if num_nt_aces > 0.50:
                                        return 5.0
                            if sum_spades_values > 40.50:
                                if num_nt_kings <= 1.50:
                                    if num_nt_kings <= 0.50:
                                        if num_nt_aces <= 0.50:
                                            if sum_spades_values <= 43.50:
                                                if num_void_suits <= 0.50:
                                                    return 3.0
                                                if num_void_suits > 0.50:
                                                    return 4.0
                                            if sum_spades_values > 43.50:
                                                return 4.0
                                        if num_nt_aces > 0.50:
                                            if sum_spades_values <= 43.00:
                                                return 4.0
                                            if sum_spades_values > 43.00:
                                                if sum_spades_values <= 48.00:
                                                    return 5.0
                                                if sum_spades_values > 48.00:
                                                    if num_void_suits <= 0.50:
                                                        return 5.0
                                                    if num_void_suits > 0.50:
                                                        return 6.0
                                    if num_nt_kings > 0.50:
                                        if sum_spades_values <= 42.50:
                                            if num_nt_aces <= 0.50:
                                                return 4.0
                                            if num_nt_aces > 0.50:
                                                return 5.0
                                        if sum_spades_values > 42.50:
                                            if num_void_suits <= 0.50:
                                                if sum_spades_values <= 46.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 4.0
                                                    if num_nt_aces > 0.50:
                                                        return 5.0
                                                if sum_spades_values > 46.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 5.0
                                                    if num_nt_aces > 0.50:
                                                        return 6.0
                                            if num_void_suits > 0.50:
                                                if num_nt_aces <= 0.50:
                                                    return 5.0
                                                if num_nt_aces > 0.50:
                                                    if sum_spades_values <= 44.00:
                                                        return 5.0
                                                    if sum_spades_values > 44.00:
                                                        return 6.0
                                if num_nt_kings > 1.50:
                                    if num_nt_aces <= 0.50:
                                        if num_nt_kings <= 2.50:
                                            if num_void_suits <= 0.50:
                                                if sum_spades_values <= 48.50:
                                                    return 5.0
                                                if sum_spades_values > 48.50:
                                                    return 6.0
                                            if num_void_suits > 0.50:
                                                if sum_spades_values <= 49.00:
                                                    return 5.0
                                                if sum_spades_values > 49.00:
                                                    return 6.0
                                        if num_nt_kings > 2.50:
                                            if sum_spades_values <= 44.00:
                                                return 5.0
                                            if sum_spades_values > 44.00:
                                                return 6.0
                                    if num_nt_aces > 0.50:
                                        if sum_spades_values <= 49.00:
                                            if num_nt_kings <= 2.50:
                                                return 6.0
                                            if num_nt_kings > 2.50:
                                                if sum_spades_values <= 44.50:
                                                    return 6.0
                                                if sum_spades_values > 44.50:
                                                    return 7.0
                                        if sum_spades_values > 49.00:
                                            return 7.0
                        if num_void_suits > 1.50:
                            if num_nt_kings <= 0.50:
                                if sum_spades_values <= 46.00:
                                    if sum_spades_values <= 40.50:
                                        if sum_spades_values <= 39.50:
                                            return 4.0
                                        if sum_spades_values > 39.50:
                                            return 5.0
                                    if sum_spades_values > 40.50:
                                        if num_nt_aces <= 0.50:
                                            if sum_spades_values <= 42.50:
                                                return 4.0
                                            if sum_spades_values > 42.50:
                                                return 3.0
                                        if num_nt_aces > 0.50:
                                            return 4.0
                                if sum_spades_values > 46.00:
                                    if sum_spades_values <= 49.00:
                                        return 5.0
                                    if sum_spades_values > 49.00:
                                        return 4.0
                            if num_nt_kings > 0.50:
                                if sum_spades_values <= 46.50:
                                    if sum_spades_values <= 44.50:
                                        if sum_spades_values <= 42.00:
                                            if num_nt_aces <= 0.50:
                                                return 4.0
                                            if num_nt_aces > 0.50:
                                                if sum_spades_values <= 40.00:
                                                    return 5.0
                                                if sum_spades_values > 40.00:
                                                    return 4.0
                                        if sum_spades_values > 42.00:
                                            return 3.0
                                    if sum_spades_values > 44.50:
                                        return 5.0
                                if sum_spades_values > 46.50:
                                    if sum_spades_values <= 47.50:
                                        return 4.0
                                    if sum_spades_values > 47.50:
                                        if sum_spades_values <= 48.50:
                                            return 5.0
                                        if sum_spades_values > 48.50:
                                            return 4.0
                if num_spades > 4.50:
                    if sum_spades_values <= 40.50:
                        if num_nt_aces <= 0.50:
                            if num_nt_kings <= 0.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 25.50:
                                        return 2.0
                                    if sum_spades_values > 25.50:
                                        if sum_spades_values <= 38.50:
                                            return 3.0
                                        if sum_spades_values > 38.50:
                                            return 4.0
                                if num_void_suits > 0.50:
                                    if num_void_suits <= 1.50:
                                        if sum_spades_values <= 38.50:
                                            return 4.0
                                        if sum_spades_values > 38.50:
                                            return 5.0
                                    if num_void_suits > 1.50:
                                        if sum_spades_values <= 28.00:
                                            return 5.0
                                        if sum_spades_values > 28.00:
                                            if sum_spades_values <= 31.00:
                                                return 4.0
                                            if sum_spades_values > 31.00:
                                                if sum_spades_values <= 32.50:
                                                    return 5.0
                                                if sum_spades_values > 32.50:
                                                    return 6.0
                            if num_nt_kings > 0.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 30.50:
                                        if sum_spades_values <= 26.50:
                                            return 4.0
                                        if sum_spades_values > 26.50:
                                            if num_nt_kings <= 1.50:
                                                return 3.0
                                            if num_nt_kings > 1.50:
                                                if sum_spades_values <= 29.50:
                                                    return 4.0
                                                if sum_spades_values > 29.50:
                                                    return 5.0
                                    if sum_spades_values > 30.50:
                                        if sum_spades_values <= 36.00:
                                            if num_nt_kings <= 2.50:
                                                return 4.0
                                            if num_nt_kings > 2.50:
                                                return 5.0
                                        if sum_spades_values > 36.00:
                                            if num_nt_kings <= 1.50:
                                                return 4.0
                                            if num_nt_kings > 1.50:
                                                return 5.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 29.50:
                                        if num_nt_kings <= 1.50:
                                            if num_void_suits <= 1.50:
                                                return 4.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 26.50:
                                                    return 5.0
                                                if sum_spades_values > 26.50:
                                                    return 6.0
                                        if num_nt_kings > 1.50:
                                            return 5.0
                                    if sum_spades_values > 29.50:
                                        if sum_spades_values <= 38.00:
                                            return 5.0
                                        if sum_spades_values > 38.00:
                                            if num_void_suits <= 1.50:
                                                if num_nt_kings <= 1.50:
                                                    return 5.0
                                                if num_nt_kings > 1.50:
                                                    return 6.0
                                            if num_void_suits > 1.50:
                                                return 5.0
                        if num_nt_aces > 0.50:
                            if num_void_suits <= 1.50:
                                if num_void_suits <= 0.50:
                                    if num_nt_kings <= 1.50:
                                        if sum_spades_values <= 30.50:
                                            return 4.0
                                        if sum_spades_values > 30.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 36.50:
                                                    return 4.0
                                                if sum_spades_values > 36.50:
                                                    return 5.0
                                            if num_nt_kings > 0.50:
                                                return 5.0
                                    if num_nt_kings > 1.50:
                                        if num_nt_kings <= 2.50:
                                            if sum_spades_values <= 35.50:
                                                return 5.0
                                            if sum_spades_values > 35.50:
                                                return 6.0
                                        if num_nt_kings > 2.50:
                                            if sum_spades_values <= 28.00:
                                                return 5.0
                                            if sum_spades_values > 28.00:
                                                return 6.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 25.50:
                                        if num_nt_kings <= 1.50:
                                            return 5.0
                                        if num_nt_kings > 1.50:
                                            return 6.0
                                    if sum_spades_values > 25.50:
                                        if sum_spades_values <= 28.00:
                                            return 6.0
                                        if sum_spades_values > 28.00:
                                            if sum_spades_values <= 35.50:
                                                if sum_spades_values <= 29.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 5.0
                                                    if num_nt_kings > 1.50:
                                                        return 6.0
                                                if sum_spades_values > 29.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 5.0
                                                    if num_nt_kings > 0.50:
                                                        return 6.0
                                            if sum_spades_values > 35.50:
                                                if num_nt_kings <= 0.50:
                                                    return 5.0
                                                if num_nt_kings > 0.50:
                                                    if sum_spades_values <= 39.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 6.0
                                                        if num_nt_kings > 1.50:
                                                            return 7.0
                                                    if sum_spades_values > 39.50:
                                                        return 6.0
                            if num_void_suits > 1.50:
                                if num_nt_kings <= 0.50:
                                    if sum_spades_values <= 36.00:
                                        if sum_spades_values <= 34.00:
                                            return 7.0
                                        if sum_spades_values > 34.00:
                                            return 6.0
                                    if sum_spades_values > 36.00:
                                        return 7.0
                                if num_nt_kings > 0.50:
                                    if sum_spades_values <= 26.50:
                                        return 8.0
                                    if sum_spades_values > 26.50:
                                        if sum_spades_values <= 32.00:
                                            if sum_spades_values <= 29.00:
                                                return 6.0
                                            if sum_spades_values > 29.00:
                                                return 7.0
                                        if sum_spades_values > 32.00:
                                            return 6.0
                    if sum_spades_values > 40.50:
                        if num_nt_aces <= 0.50:
                            if num_nt_kings <= 2.50:
                                if num_nt_kings <= 1.50:
                                    if num_nt_kings <= 0.50:
                                        if num_void_suits <= 1.50:
                                            if sum_spades_values <= 50.50:
                                                if num_void_suits <= 0.50:
                                                    return 4.0
                                                if num_void_suits > 0.50:
                                                    return 5.0
                                            if sum_spades_values > 50.50:
                                                if num_void_suits <= 0.50:
                                                    return 5.0
                                                if num_void_suits > 0.50:
                                                    if sum_spades_values <= 53.50:
                                                        return 5.0
                                                    if sum_spades_values > 53.50:
                                                        return 6.0
                                        if num_void_suits > 1.50:
                                            if sum_spades_values <= 52.50:
                                                if sum_spades_values <= 43.50:
                                                    if sum_spades_values <= 42.50:
                                                        return 6.0
                                                    if sum_spades_values > 42.50:
                                                        return 5.0
                                                if sum_spades_values > 43.50:
                                                    return 6.0
                                            if sum_spades_values > 52.50:
                                                if sum_spades_values <= 55.50:
                                                    return 7.0
                                                if sum_spades_values > 55.50:
                                                    return 9.0
                                    if num_nt_kings > 0.50:
                                        if num_void_suits <= 1.50:
                                            if num_void_suits <= 0.50:
                                                if sum_spades_values <= 55.00:
                                                    if sum_spades_values <= 43.00:
                                                        return 4.0
                                                    if sum_spades_values > 43.00:
                                                        return 5.0
                                                if sum_spades_values > 55.00:
                                                    return 6.0
                                            if num_void_suits > 0.50:
                                                if sum_spades_values <= 48.50:
                                                    return 5.0
                                                if sum_spades_values > 48.50:
                                                    return 6.0
                                        if num_void_suits > 1.50:
                                            if sum_spades_values <= 53.00:
                                                return 6.0
                                            if sum_spades_values > 53.00:
                                                if sum_spades_values <= 56.50:
                                                    return 7.0
                                                if sum_spades_values > 56.50:
                                                    if sum_spades_values <= 59.00:
                                                        return 8.0
                                                    if sum_spades_values > 59.00:
                                                        return 5.0
                                if num_nt_kings > 1.50:
                                    if sum_spades_values <= 47.00:
                                        if num_void_suits <= 0.50:
                                            return 5.0
                                        if num_void_suits > 0.50:
                                            return 6.0
                                    if sum_spades_values > 47.00:
                                        if num_void_suits <= 0.50:
                                            return 6.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 51.50:
                                                return 6.0
                                            if sum_spades_values > 51.50:
                                                return 7.0
                            if num_nt_kings > 2.50:
                                if sum_spades_values <= 52.50:
                                    return 6.0
                                if sum_spades_values > 52.50:
                                    return 7.0
                        if num_nt_aces > 0.50:
                            if num_nt_kings <= 1.50:
                                if num_void_suits <= 0.50:
                                    if num_nt_kings <= 0.50:
                                        if sum_spades_values <= 50.50:
                                            return 5.0
                                        if sum_spades_values > 50.50:
                                            if sum_spades_values <= 59.50:
                                                return 6.0
                                            if sum_spades_values > 59.50:
                                                return 7.0
                                    if num_nt_kings > 0.50:
                                        if sum_spades_values <= 53.00:
                                            if sum_spades_values <= 43.50:
                                                return 5.0
                                            if sum_spades_values > 43.50:
                                                return 6.0
                                        if sum_spades_values > 53.00:
                                            return 7.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 45.50:
                                        if num_void_suits <= 1.50:
                                            return 6.0
                                        if num_void_suits > 1.50:
                                            if sum_spades_values <= 42.50:
                                                if sum_spades_values <= 41.50:
                                                    return 6.0
                                                if sum_spades_values > 41.50:
                                                    return 7.0
                                            if sum_spades_values > 42.50:
                                                return 6.0
                                    if sum_spades_values > 45.50:
                                        if sum_spades_values <= 54.50:
                                            if num_nt_kings <= 0.50:
                                                if num_void_suits <= 1.50:
                                                    return 6.0
                                                if num_void_suits > 1.50:
                                                    if sum_spades_values <= 52.50:
                                                        return 7.0
                                                    if sum_spades_values > 52.50:
                                                        return 8.0
                                            if num_nt_kings > 0.50:
                                                if num_void_suits <= 1.50:
                                                    return 7.0
                                                if num_void_suits > 1.50:
                                                    if sum_spades_values <= 49.00:
                                                        return 7.0
                                                    if sum_spades_values > 49.00:
                                                        return 6.0
                                        if sum_spades_values > 54.50:
                                            if sum_spades_values <= 58.50:
                                                return 7.0
                                            if sum_spades_values > 58.50:
                                                if sum_spades_values <= 59.50:
                                                    return 9.0
                                                if sum_spades_values > 59.50:
                                                    return 7.0
                            if num_nt_kings > 1.50:
                                if sum_spades_values <= 51.50:
                                    if sum_spades_values <= 47.50:
                                        if num_void_suits <= 0.50:
                                            if sum_spades_values <= 45.50:
                                                if num_nt_kings <= 2.50:
                                                    return 6.0
                                                if num_nt_kings > 2.50:
                                                    return 7.0
                                            if sum_spades_values > 45.50:
                                                return 6.0
                                        if num_void_suits > 0.50:
                                            return 7.0
                                    if sum_spades_values > 47.50:
                                        return 7.0
                                if sum_spades_values > 51.50:
                                    if sum_spades_values <= 57.50:
                                        if num_nt_kings <= 2.50:
                                            if num_void_suits <= 0.50:
                                                return 7.0
                                            if num_void_suits > 0.50:
                                                return 8.0
                                        if num_nt_kings > 2.50:
                                            return 8.0
                                    if sum_spades_values > 57.50:
                                        return 8.0
            if num_nt_aces > 1.50:
                if sum_spades_values <= 40.50:
                    if num_nt_aces <= 2.50:
                        if num_spades <= 3.50:
                            if num_nt_kings <= 1.50:
                                if sum_spades_values <= 31.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 29.50:
                                            if sum_spades_values <= 27.50:
                                                if num_nt_kings <= 0.50:
                                                    return 4.0
                                                if num_nt_kings > 0.50:
                                                    if num_spades <= 2.50:
                                                        return 5.0
                                                    if num_spades > 2.50:
                                                        return 4.0
                                            if sum_spades_values > 27.50:
                                                return 4.0
                                        if sum_spades_values > 29.50:
                                            if num_nt_kings <= 0.50:
                                                return 4.0
                                            if num_nt_kings > 0.50:
                                                return 5.0
                                    if num_void_suits > 0.50:
                                        if num_nt_kings <= 0.50:
                                            return 5.0
                                        if num_nt_kings > 0.50:
                                            if num_spades <= 2.50:
                                                return 4.0
                                            if num_spades > 2.50:
                                                return 5.0
                                if sum_spades_values > 31.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 38.00:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 35.00:
                                                    return 4.0
                                                if sum_spades_values > 35.00:
                                                    return 5.0
                                            if num_nt_kings > 0.50:
                                                return 5.0
                                        if sum_spades_values > 38.00:
                                            return 6.0
                                    if num_void_suits > 0.50:
                                        return 5.0
                            if num_nt_kings > 1.50:
                                if num_nt_kings <= 2.50:
                                    if num_spades <= 2.50:
                                        return 5.0
                                    if num_spades > 2.50:
                                        if sum_spades_values <= 32.50:
                                            if sum_spades_values <= 29.50:
                                                if sum_spades_values <= 28.50:
                                                    if num_void_suits <= 0.50:
                                                        return 5.0
                                                    if num_void_suits > 0.50:
                                                        if sum_spades_values <= 26.00:
                                                            return 5.0
                                                        if sum_spades_values > 26.00:
                                                            return 6.0
                                                if sum_spades_values > 28.50:
                                                    return 6.0
                                            if sum_spades_values > 29.50:
                                                return 5.0
                                        if sum_spades_values > 32.50:
                                            return 6.0
                                if num_nt_kings > 2.50:
                                    if sum_spades_values <= 36.00:
                                        if num_spades <= 2.50:
                                            if sum_spades_values <= 26.00:
                                                return 5.0
                                            if sum_spades_values > 26.00:
                                                return 6.0
                                        if num_spades > 2.50:
                                            return 6.0
                                    if sum_spades_values > 36.00:
                                        return 7.0
                        if num_spades > 3.50:
                            if num_void_suits <= 0.50:
                                if num_nt_kings <= 1.50:
                                    if num_spades <= 4.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 31.00:
                                                return 4.0
                                            if sum_spades_values > 31.00:
                                                return 5.0
                                        if num_nt_kings > 0.50:
                                            if sum_spades_values <= 35.50:
                                                return 5.0
                                            if sum_spades_values > 35.50:
                                                return 6.0
                                    if num_spades > 4.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 38.00:
                                                return 5.0
                                            if sum_spades_values > 38.00:
                                                return 6.0
                                        if num_nt_kings > 0.50:
                                            if sum_spades_values <= 30.50:
                                                return 5.0
                                            if sum_spades_values > 30.50:
                                                return 6.0
                                if num_nt_kings > 1.50:
                                    if num_spades <= 4.50:
                                        if sum_spades_values <= 26.50:
                                            return 5.0
                                        if sum_spades_values > 26.50:
                                            if sum_spades_values <= 39.50:
                                                if num_nt_kings <= 2.50:
                                                    return 6.0
                                                if num_nt_kings > 2.50:
                                                    if sum_spades_values <= 32.00:
                                                        return 6.0
                                                    if sum_spades_values > 32.00:
                                                        return 7.0
                                            if sum_spades_values > 39.50:
                                                return 7.0
                                    if num_spades > 4.50:
                                        if sum_spades_values <= 33.00:
                                            if num_nt_kings <= 2.50:
                                                return 6.0
                                            if num_nt_kings > 2.50:
                                                if sum_spades_values <= 28.50:
                                                    return 6.0
                                                if sum_spades_values > 28.50:
                                                    return 7.0
                                        if sum_spades_values > 33.00:
                                            return 7.0
                            if num_void_suits > 0.50:
                                if num_spades <= 4.50:
                                    if num_nt_kings <= 1.50:
                                        if sum_spades_values <= 29.00:
                                            return 5.0
                                        if sum_spades_values > 29.00:
                                            return 6.0
                                    if num_nt_kings > 1.50:
                                        if sum_spades_values <= 30.00:
                                            return 6.0
                                        if sum_spades_values > 30.00:
                                            return 7.0
                                if num_spades > 4.50:
                                    if sum_spades_values <= 30.50:
                                        if sum_spades_values <= 28.50:
                                            if sum_spades_values <= 25.50:
                                                if num_nt_kings <= 1.50:
                                                    return 6.0
                                                if num_nt_kings > 1.50:
                                                    return 7.0
                                            if sum_spades_values > 25.50:
                                                if num_nt_kings <= 1.00:
                                                    return 6.0
                                                if num_nt_kings > 1.00:
                                                    return 7.0
                                        if sum_spades_values > 28.50:
                                            if sum_spades_values <= 29.50:
                                                return 6.0
                                            if sum_spades_values > 29.50:
                                                if num_nt_kings <= 1.00:
                                                    return 6.0
                                                if num_nt_kings > 1.00:
                                                    return 7.0
                                    if sum_spades_values > 30.50:
                                        if sum_spades_values <= 39.50:
                                            if num_nt_kings <= 0.50:
                                                return 6.0
                                            if num_nt_kings > 0.50:
                                                return 7.0
                                        if sum_spades_values > 39.50:
                                            return 6.0
                    if num_nt_aces > 2.50:
                        if num_nt_kings <= 0.50:
                            if sum_spades_values <= 35.00:
                                if sum_spades_values <= 29.50:
                                    if num_spades <= 4.50:
                                        return 5.0
                                    if num_spades > 4.50:
                                        if sum_spades_values <= 27.50:
                                            return 5.0
                                        if sum_spades_values > 27.50:
                                            return 6.0
                                if sum_spades_values > 29.50:
                                    if sum_spades_values <= 31.00:
                                        if num_spades <= 4.00:
                                            return 5.0
                                        if num_spades > 4.00:
                                            return 6.0
                                    if sum_spades_values > 31.00:
                                        if sum_spades_values <= 32.50:
                                            if num_spades <= 4.00:
                                                return 5.0
                                            if num_spades > 4.00:
                                                return 6.0
                                        if sum_spades_values > 32.50:
                                            if sum_spades_values <= 33.50:
                                                if num_spades <= 4.00:
                                                    return 5.0
                                                if num_spades > 4.00:
                                                    return 6.0
                                            if sum_spades_values > 33.50:
                                                if num_spades <= 3.50:
                                                    return 5.0
                                                if num_spades > 3.50:
                                                    return 6.0
                            if sum_spades_values > 35.00:
                                return 6.0
                        if num_nt_kings > 0.50:
                            if num_spades <= 4.50:
                                if sum_spades_values <= 31.50:
                                    if num_spades <= 3.50:
                                        if sum_spades_values <= 28.00:
                                            if num_nt_kings <= 2.50:
                                                return 6.0
                                            if num_nt_kings > 2.50:
                                                return 7.0
                                        if sum_spades_values > 28.00:
                                            return 6.0
                                    if num_spades > 3.50:
                                        if sum_spades_values <= 29.50:
                                            if num_nt_kings <= 2.50:
                                                if sum_spades_values <= 28.50:
                                                    return 6.0
                                                if sum_spades_values > 28.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 6.0
                                                    if num_nt_kings > 1.50:
                                                        return 7.0
                                            if num_nt_kings > 2.50:
                                                return 7.0
                                        if sum_spades_values > 29.50:
                                            if sum_spades_values <= 30.50:
                                                return 7.0
                                            if sum_spades_values > 30.50:
                                                if num_nt_kings <= 2.00:
                                                    return 6.0
                                                if num_nt_kings > 2.00:
                                                    return 7.0
                                if sum_spades_values > 31.50:
                                    if num_nt_kings <= 2.50:
                                        if sum_spades_values <= 35.50:
                                            if sum_spades_values <= 34.50:
                                                if num_nt_kings <= 1.50:
                                                    return 6.0
                                                if num_nt_kings > 1.50:
                                                    return 7.0
                                            if sum_spades_values > 34.50:
                                                return 6.0
                                        if sum_spades_values > 35.50:
                                            if sum_spades_values <= 39.50:
                                                return 7.0
                                            if sum_spades_values > 39.50:
                                                if num_nt_kings <= 1.50:
                                                    return 7.0
                                                if num_nt_kings > 1.50:
                                                    return 8.0
                                    if num_nt_kings > 2.50:
                                        if sum_spades_values <= 34.50:
                                            return 7.0
                                        if sum_spades_values > 34.50:
                                            return 8.0
                            if num_spades > 4.50:
                                if sum_spades_values <= 36.50:
                                    if num_nt_kings <= 2.50:
                                        if num_nt_kings <= 1.50:
                                            if sum_spades_values <= 31.50:
                                                return 6.0
                                            if sum_spades_values > 31.50:
                                                return 7.0
                                        if num_nt_kings > 1.50:
                                            return 7.0
                                    if num_nt_kings > 2.50:
                                        if sum_spades_values <= 28.00:
                                            return 7.0
                                        if sum_spades_values > 28.00:
                                            return 8.0
                                if sum_spades_values > 36.50:
                                    if num_nt_kings <= 2.50:
                                        if sum_spades_values <= 38.50:
                                            if num_nt_kings <= 1.50:
                                                return 7.0
                                            if num_nt_kings > 1.50:
                                                return 8.0
                                        if sum_spades_values > 38.50:
                                            return 7.0
                                    if num_nt_kings > 2.50:
                                        return 9.0
                if sum_spades_values > 40.50:
                    if num_spades <= 4.50:
                        if num_nt_aces <= 2.50:
                            if num_nt_kings <= 0.50:
                                if sum_spades_values <= 49.50:
                                    if sum_spades_values <= 44.00:
                                        if sum_spades_values <= 41.50:
                                            return 6.0
                                        if sum_spades_values > 41.50:
                                            if num_void_suits <= 0.50:
                                                return 5.0
                                            if num_void_suits > 0.50:
                                                return 6.0
                                    if sum_spades_values > 44.00:
                                        return 6.0
                                if sum_spades_values > 49.50:
                                    if num_void_suits <= 0.50:
                                        return 6.0
                                    if num_void_suits > 0.50:
                                        return 7.0
                            if num_nt_kings > 0.50:
                                if sum_spades_values <= 41.50:
                                    return 6.0
                                if sum_spades_values > 41.50:
                                    if sum_spades_values <= 46.50:
                                        if sum_spades_values <= 43.50:
                                            if num_nt_kings <= 1.50:
                                                return 6.0
                                            if num_nt_kings > 1.50:
                                                return 7.0
                                        if sum_spades_values > 43.50:
                                            if num_void_suits <= 0.50:
                                                if num_nt_kings <= 1.50:
                                                    return 6.0
                                                if num_nt_kings > 1.50:
                                                    return 7.0
                                            if num_void_suits > 0.50:
                                                return 7.0
                                    if sum_spades_values > 46.50:
                                        if sum_spades_values <= 48.50:
                                            return 7.0
                                        if sum_spades_values > 48.50:
                                            if num_nt_kings <= 2.50:
                                                return 7.0
                                            if num_nt_kings > 2.50:
                                                return 8.0
                        if num_nt_aces > 2.50:
                            if sum_spades_values <= 46.50:
                                if num_nt_kings <= 1.50:
                                    if sum_spades_values <= 43.50:
                                        if sum_spades_values <= 42.50:
                                            if num_nt_kings <= 0.50:
                                                return 6.0
                                            if num_nt_kings > 0.50:
                                                return 7.0
                                        if sum_spades_values > 42.50:
                                            if num_nt_kings <= 0.50:
                                                return 6.0
                                            if num_nt_kings > 0.50:
                                                return 7.0
                                    if sum_spades_values > 43.50:
                                        return 7.0
                                if num_nt_kings > 1.50:
                                    if sum_spades_values <= 44.50:
                                        return 8.0
                                    if sum_spades_values > 44.50:
                                        return 9.0
                            if sum_spades_values > 46.50:
                                if num_nt_kings <= 2.50:
                                    return 8.0
                                if num_nt_kings > 2.50:
                                    if sum_spades_values <= 48.50:
                                        return 9.0
                                    if sum_spades_values > 48.50:
                                        if sum_spades_values <= 49.50:
                                            return 10.0
                                        if sum_spades_values > 49.50:
                                            return 9.0
                    if num_spades > 4.50:
                        if sum_spades_values <= 50.50:
                            if num_void_suits <= 0.50:
                                if sum_spades_values <= 47.50:
                                    if num_nt_aces <= 2.50:
                                        if sum_spades_values <= 45.50:
                                            if sum_spades_values <= 42.00:
                                                if num_nt_kings <= 1.50:
                                                    return 6.0
                                                if num_nt_kings > 1.50:
                                                    return 7.0
                                            if sum_spades_values > 42.00:
                                                if sum_spades_values <= 44.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 7.0
                                                    if num_nt_kings > 2.50:
                                                        return 8.0
                                                if sum_spades_values > 44.50:
                                                    if num_nt_kings <= 2.50:
                                                        if num_nt_kings <= 1.00:
                                                            return 6.0
                                                        if num_nt_kings > 1.00:
                                                            return 7.0
                                                    if num_nt_kings > 2.50:
                                                        return 8.0
                                        if sum_spades_values > 45.50:
                                            if num_nt_kings <= 1.50:
                                                return 6.0
                                            if num_nt_kings > 1.50:
                                                return 8.0
                                    if num_nt_aces > 2.50:
                                        if sum_spades_values <= 46.50:
                                            if num_nt_kings <= 0.50:
                                                return 7.0
                                            if num_nt_kings > 0.50:
                                                if sum_spades_values <= 44.50:
                                                    if sum_spades_values <= 41.50:
                                                        if num_nt_kings <= 2.50:
                                                            return 8.0
                                                        if num_nt_kings > 2.50:
                                                            return 9.0
                                                    if sum_spades_values > 41.50:
                                                        return 8.0
                                                if sum_spades_values > 44.50:
                                                    return 9.0
                                        if sum_spades_values > 46.50:
                                            if num_nt_kings <= 1.50:
                                                return 8.0
                                            if num_nt_kings > 1.50:
                                                return 9.0
                                if sum_spades_values > 47.50:
                                    if sum_spades_values <= 49.50:
                                        if sum_spades_values <= 48.50:
                                            if num_nt_kings <= 1.50:
                                                return 7.0
                                            if num_nt_kings > 1.50:
                                                if num_nt_aces <= 2.50:
                                                    return 8.0
                                                if num_nt_aces > 2.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 9.0
                                                    if num_nt_kings > 2.50:
                                                        return 10.0
                                        if sum_spades_values > 48.50:
                                            if num_nt_kings <= 1.50:
                                                if num_nt_kings <= 0.50:
                                                    if num_nt_aces <= 2.50:
                                                        return 6.0
                                                    if num_nt_aces > 2.50:
                                                        return 7.0
                                                if num_nt_kings > 0.50:
                                                    return 7.0
                                            if num_nt_kings > 1.50:
                                                if num_nt_aces <= 2.50:
                                                    return 8.0
                                                if num_nt_aces > 2.50:
                                                    return 9.0
                                    if sum_spades_values > 49.50:
                                        if num_nt_aces <= 2.50:
                                            if num_nt_kings <= 1.50:
                                                return 7.0
                                            if num_nt_kings > 1.50:
                                                return 8.0
                                        if num_nt_aces > 2.50:
                                            if num_nt_kings <= 0.50:
                                                return 7.0
                                            if num_nt_kings > 0.50:
                                                return 8.0
                            if num_void_suits > 0.50:
                                if sum_spades_values <= 42.50:
                                    return 7.0
                                if sum_spades_values > 42.50:
                                    if num_nt_kings <= 0.50:
                                        return 7.0
                                    if num_nt_kings > 0.50:
                                        if sum_spades_values <= 47.50:
                                            if num_nt_kings <= 1.50:
                                                return 7.0
                                            if num_nt_kings > 1.50:
                                                return 8.0
                                        if sum_spades_values > 47.50:
                                            return 8.0
                        if sum_spades_values > 50.50:
                            if num_nt_kings <= 1.50:
                                if num_nt_aces <= 2.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 59.50:
                                                return 7.0
                                            if sum_spades_values > 59.50:
                                                return 8.0
                                        if num_nt_kings > 0.50:
                                            if sum_spades_values <= 53.50:
                                                return 7.0
                                            if sum_spades_values > 53.50:
                                                return 8.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 59.50:
                                            if sum_spades_values <= 52.50:
                                                if num_nt_kings <= 0.50:
                                                    return 7.0
                                                if num_nt_kings > 0.50:
                                                    return 8.0
                                            if sum_spades_values > 52.50:
                                                return 8.0
                                        if sum_spades_values > 59.50:
                                            if num_nt_kings <= 0.50:
                                                return 8.0
                                            if num_nt_kings > 0.50:
                                                return 9.0
                                if num_nt_aces > 2.50:
                                    if sum_spades_values <= 53.50:
                                        return 8.0
                                    if sum_spades_values > 53.50:
                                        if sum_spades_values <= 54.50:
                                            return 9.0
                                        if sum_spades_values > 54.50:
                                            if num_nt_kings <= 0.50:
                                                return 8.0
                                            if num_nt_kings > 0.50:
                                                return 9.0
                            if num_nt_kings > 1.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 51.50:
                                        return 9.0
                                    if sum_spades_values > 51.50:
                                        if num_nt_aces <= 2.50:
                                            if num_nt_kings <= 2.50:
                                                if sum_spades_values <= 57.00:
                                                    return 8.0
                                                if sum_spades_values > 57.00:
                                                    return 9.0
                                            if num_nt_kings > 2.50:
                                                return 9.0
                                        if num_nt_aces > 2.50:
                                            if sum_spades_values <= 56.50:
                                                if sum_spades_values <= 55.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 9.0
                                                    if num_nt_kings > 2.50:
                                                        return 10.0
                                                if sum_spades_values > 55.50:
                                                    return 10.0
                                            if sum_spades_values > 56.50:
                                                if num_nt_kings <= 2.50:
                                                    if sum_spades_values <= 58.00:
                                                        return 9.0
                                                    if sum_spades_values > 58.00:
                                                        return 10.0
                                                if num_nt_kings > 2.50:
                                                    if sum_spades_values <= 58.00:
                                                        return 10.0
                                                    if sum_spades_values > 58.00:
                                                        return 9.0
                                if num_void_suits > 0.50:
                                    return 9.0
    if num_spades > 5.50:
        if sum_spades_values <= 59.50:
            if sum_spades_values <= 45.50:
                if num_nt_aces <= 1.50:
                    if num_nt_kings <= 1.50:
                        if num_void_suits <= 1.50:
                            if num_void_suits <= 0.50:
                                if num_nt_aces <= 0.50:
                                    if num_spades <= 7.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 33.50:
                                                return 3.0
                                            if sum_spades_values > 33.50:
                                                if num_spades <= 6.50:
                                                    return 4.0
                                                if num_spades > 6.50:
                                                    if sum_spades_values <= 41.00:
                                                        return 4.0
                                                    if sum_spades_values > 41.00:
                                                        return 5.0
                                        if num_nt_kings > 0.50:
                                            if num_spades <= 6.50:
                                                if sum_spades_values <= 36.00:
                                                    return 4.0
                                                if sum_spades_values > 36.00:
                                                    return 5.0
                                            if num_spades > 6.50:
                                                return 5.0
                                    if num_spades > 7.50:
                                        return 6.0
                                if num_nt_aces > 0.50:
                                    if sum_spades_values <= 36.50:
                                        if sum_spades_values <= 32.50:
                                            if num_nt_kings <= 0.50:
                                                return 4.0
                                            if num_nt_kings > 0.50:
                                                return 5.0
                                        if sum_spades_values > 32.50:
                                            if sum_spades_values <= 33.50:
                                                if num_nt_kings <= 0.50:
                                                    return 4.0
                                                if num_nt_kings > 0.50:
                                                    return 5.0
                                            if sum_spades_values > 33.50:
                                                return 5.0
                                    if sum_spades_values > 36.50:
                                        if num_spades <= 7.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 40.50:
                                                    return 5.0
                                                if sum_spades_values > 40.50:
                                                    if sum_spades_values <= 42.00:
                                                        if num_spades <= 6.50:
                                                            return 5.0
                                                        if num_spades > 6.50:
                                                            return 6.0
                                                    if sum_spades_values > 42.00:
                                                        return 5.0
                                            if num_nt_kings > 0.50:
                                                if num_spades <= 6.50:
                                                    if sum_spades_values <= 37.50:
                                                        return 5.0
                                                    if sum_spades_values > 37.50:
                                                        return 6.0
                                                if num_spades > 6.50:
                                                    return 6.0
                                        if num_spades > 7.50:
                                            if num_nt_kings <= 0.50:
                                                return 6.0
                                            if num_nt_kings > 0.50:
                                                return 7.0
                            if num_void_suits > 0.50:
                                if num_nt_kings <= 0.50:
                                    if num_nt_aces <= 0.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 34.50:
                                                return 4.0
                                            if sum_spades_values > 34.50:
                                                return 5.0
                                        if num_spades > 6.50:
                                            if num_spades <= 7.50:
                                                if sum_spades_values <= 42.00:
                                                    return 5.0
                                                if sum_spades_values > 42.00:
                                                    return 6.0
                                            if num_spades > 7.50:
                                                return 6.0
                                    if num_nt_aces > 0.50:
                                        if sum_spades_values <= 33.50:
                                            return 5.0
                                        if sum_spades_values > 33.50:
                                            if num_spades <= 7.50:
                                                return 6.0
                                            if num_spades > 7.50:
                                                return 7.0
                                if num_nt_kings > 0.50:
                                    if num_spades <= 6.50:
                                        if sum_spades_values <= 38.00:
                                            if sum_spades_values <= 35.50:
                                                if num_nt_aces <= 0.50:
                                                    return 5.0
                                                if num_nt_aces > 0.50:
                                                    return 6.0
                                            if sum_spades_values > 35.50:
                                                return 5.0
                                        if sum_spades_values > 38.00:
                                            if sum_spades_values <= 40.50:
                                                return 7.0
                                            if sum_spades_values > 40.50:
                                                if sum_spades_values <= 42.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 6.0
                                                    if num_nt_aces > 0.50:
                                                        return 7.0
                                                if sum_spades_values > 42.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 6.0
                                                    if num_nt_aces > 0.50:
                                                        return 7.0
                                    if num_spades > 6.50:
                                        if sum_spades_values <= 44.50:
                                            if num_nt_aces <= 0.50:
                                                if sum_spades_values <= 43.50:
                                                    return 6.0
                                                if sum_spades_values > 43.50:
                                                    if num_spades <= 7.50:
                                                        return 6.0
                                                    if num_spades > 7.50:
                                                        return 7.0
                                            if num_nt_aces > 0.50:
                                                if num_spades <= 7.50:
                                                    if sum_spades_values <= 35.50:
                                                        return 6.0
                                                    if sum_spades_values > 35.50:
                                                        return 7.0
                                                if num_spades > 7.50:
                                                    return 7.0
                                        if sum_spades_values > 44.50:
                                            return 8.0
                        if num_void_suits > 1.50:
                            if num_nt_kings <= 0.50:
                                if num_nt_aces <= 0.50:
                                    if num_spades <= 6.50:
                                        if sum_spades_values <= 35.50:
                                            if sum_spades_values <= 29.50:
                                                return 7.0
                                            if sum_spades_values > 29.50:
                                                if sum_spades_values <= 31.50:
                                                    return 5.0
                                                if sum_spades_values > 31.50:
                                                    return 6.0
                                        if sum_spades_values > 35.50:
                                            return 7.0
                                    if num_spades > 6.50:
                                        if sum_spades_values <= 43.50:
                                            if sum_spades_values <= 38.00:
                                                if sum_spades_values <= 35.50:
                                                    return 7.0
                                                if sum_spades_values > 35.50:
                                                    return 8.0
                                            if sum_spades_values > 38.00:
                                                return 7.0
                                        if sum_spades_values > 43.50:
                                            return 8.0
                                if num_nt_aces > 0.50:
                                    if sum_spades_values <= 32.00:
                                        return 7.0
                                    if sum_spades_values > 32.00:
                                        if num_spades <= 6.50:
                                            return 8.0
                                        if num_spades > 6.50:
                                            if sum_spades_values <= 36.00:
                                                return 6.0
                                            if sum_spades_values > 36.00:
                                                return 8.0
                            if num_nt_kings > 0.50:
                                if num_nt_aces <= 0.50:
                                    if sum_spades_values <= 38.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 28.00:
                                                return 5.0
                                            if sum_spades_values > 28.00:
                                                if sum_spades_values <= 31.50:
                                                    return 6.0
                                                if sum_spades_values > 31.50:
                                                    return 7.0
                                        if num_spades > 6.50:
                                            if sum_spades_values <= 37.50:
                                                return 8.0
                                            if sum_spades_values > 37.50:
                                                return 6.0
                                    if sum_spades_values > 38.50:
                                        if sum_spades_values <= 41.50:
                                            return 7.0
                                        if sum_spades_values > 41.50:
                                            if num_spades <= 6.50:
                                                return 7.0
                                            if num_spades > 6.50:
                                                return 8.0
                                if num_nt_aces > 0.50:
                                    if sum_spades_values <= 29.50:
                                        return 6.0
                                    if sum_spades_values > 29.50:
                                        if num_spades <= 6.50:
                                            return 8.0
                                        if num_spades > 6.50:
                                            return 9.0
                    if num_nt_kings > 1.50:
                        if num_nt_aces <= 0.50:
                            if num_void_suits <= 0.50:
                                if num_nt_kings <= 2.50:
                                    if num_spades <= 6.50:
                                        if sum_spades_values <= 30.50:
                                            return 4.0
                                        if sum_spades_values > 30.50:
                                            if sum_spades_values <= 41.50:
                                                return 5.0
                                            if sum_spades_values > 41.50:
                                                return 6.0
                                    if num_spades > 6.50:
                                        if sum_spades_values <= 38.50:
                                            return 5.0
                                        if sum_spades_values > 38.50:
                                            if num_spades <= 7.50:
                                                return 6.0
                                            if num_spades > 7.50:
                                                if sum_spades_values <= 44.50:
                                                    return 6.0
                                                if sum_spades_values > 44.50:
                                                    return 7.0
                                if num_nt_kings > 2.50:
                                    if sum_spades_values <= 38.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 37.50:
                                                return 5.0
                                            if sum_spades_values > 37.50:
                                                return 6.0
                                        if num_spades > 6.50:
                                            return 5.0
                                    if sum_spades_values > 38.50:
                                        return 6.0
                            if num_void_suits > 0.50:
                                if num_spades <= 7.50:
                                    if sum_spades_values <= 42.50:
                                        return 6.0
                                    if sum_spades_values > 42.50:
                                        return 7.0
                                if num_spades > 7.50:
                                    return 7.0
                        if num_nt_aces > 0.50:
                            if num_spades <= 6.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 40.50:
                                        if sum_spades_values <= 29.50:
                                            if num_nt_kings <= 2.50:
                                                return 5.0
                                            if num_nt_kings > 2.50:
                                                return 6.0
                                        if sum_spades_values > 29.50:
                                            if sum_spades_values <= 36.50:
                                                return 6.0
                                            if sum_spades_values > 36.50:
                                                if sum_spades_values <= 38.50:
                                                    if sum_spades_values <= 37.50:
                                                        return 7.0
                                                    if sum_spades_values > 37.50:
                                                        if num_nt_kings <= 2.50:
                                                            return 6.0
                                                        if num_nt_kings > 2.50:
                                                            return 7.0
                                                if sum_spades_values > 38.50:
                                                    return 6.0
                                    if sum_spades_values > 40.50:
                                        if sum_spades_values <= 42.50:
                                            if num_nt_kings <= 2.50:
                                                return 6.0
                                            if num_nt_kings > 2.50:
                                                return 7.0
                                        if sum_spades_values > 42.50:
                                            return 7.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 30.50:
                                        return 6.0
                                    if sum_spades_values > 30.50:
                                        if sum_spades_values <= 42.50:
                                            return 7.0
                                        if sum_spades_values > 42.50:
                                            return 8.0
                            if num_spades > 6.50:
                                if sum_spades_values <= 36.50:
                                    return 6.0
                                if sum_spades_values > 36.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 38.50:
                                            if sum_spades_values <= 37.50:
                                                return 7.0
                                            if sum_spades_values > 37.50:
                                                return 6.0
                                        if sum_spades_values > 38.50:
                                            return 7.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 38.50:
                                            return 7.0
                                        if sum_spades_values > 38.50:
                                            return 8.0
                if num_nt_aces > 1.50:
                    if num_spades <= 6.50:
                        if sum_spades_values <= 33.50:
                            if num_void_suits <= 0.50:
                                if num_nt_kings <= 1.50:
                                    if num_nt_aces <= 2.50:
                                        if num_nt_kings <= 0.50:
                                            return 5.0
                                        if num_nt_kings > 0.50:
                                            return 6.0
                                    if num_nt_aces > 2.50:
                                        if num_nt_kings <= 0.50:
                                            return 6.0
                                        if num_nt_kings > 0.50:
                                            return 7.0
                                if num_nt_kings > 1.50:
                                    if sum_spades_values <= 27.50:
                                        return 7.0
                                    if sum_spades_values > 27.50:
                                        if sum_spades_values <= 31.50:
                                            if sum_spades_values <= 28.50:
                                                if num_nt_aces <= 2.50:
                                                    return 6.0
                                                if num_nt_aces > 2.50:
                                                    return 7.0
                                            if sum_spades_values > 28.50:
                                                if num_nt_kings <= 2.50:
                                                    if num_nt_aces <= 2.50:
                                                        return 6.0
                                                    if num_nt_aces > 2.50:
                                                        return 8.0
                                                if num_nt_kings > 2.50:
                                                    return 7.0
                                        if sum_spades_values > 31.50:
                                            return 7.0
                            if num_void_suits > 0.50:
                                if sum_spades_values <= 28.00:
                                    return 6.0
                                if sum_spades_values > 28.00:
                                    if sum_spades_values <= 31.00:
                                        if num_nt_kings <= 0.50:
                                            return 6.0
                                        if num_nt_kings > 0.50:
                                            return 7.0
                                    if sum_spades_values > 31.00:
                                        if num_nt_kings <= 0.50:
                                            return 6.0
                                        if num_nt_kings > 0.50:
                                            if num_nt_kings <= 1.50:
                                                return 7.0
                                            if num_nt_kings > 1.50:
                                                return 8.0
                        if sum_spades_values > 33.50:
                            if sum_spades_values <= 39.50:
                                if num_nt_aces <= 2.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_kings <= 0.50:
                                            return 6.0
                                        if num_nt_kings > 0.50:
                                            if sum_spades_values <= 35.50:
                                                if num_nt_kings <= 1.50:
                                                    return 6.0
                                                if num_nt_kings > 1.50:
                                                    return 7.0
                                            if sum_spades_values > 35.50:
                                                if num_nt_kings <= 2.50:
                                                    return 7.0
                                                if num_nt_kings > 2.50:
                                                    if sum_spades_values <= 37.00:
                                                        return 7.0
                                                    if sum_spades_values > 37.00:
                                                        return 8.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 35.50:
                                            return 8.0
                                        if sum_spades_values > 35.50:
                                            if sum_spades_values <= 36.50:
                                                if num_nt_kings <= 1.50:
                                                    return 7.0
                                                if num_nt_kings > 1.50:
                                                    return 8.0
                                            if sum_spades_values > 36.50:
                                                return 7.0
                                if num_nt_aces > 2.50:
                                    if num_nt_kings <= 1.50:
                                        if sum_spades_values <= 37.50:
                                            return 7.0
                                        if sum_spades_values > 37.50:
                                            if sum_spades_values <= 38.50:
                                                if num_nt_kings <= 0.50:
                                                    return 7.0
                                                if num_nt_kings > 0.50:
                                                    return 8.0
                                            if sum_spades_values > 38.50:
                                                if num_nt_kings <= 0.50:
                                                    return 7.0
                                                if num_nt_kings > 0.50:
                                                    return 8.0
                                    if num_nt_kings > 1.50:
                                        if num_nt_kings <= 2.50:
                                            return 8.0
                                        if num_nt_kings > 2.50:
                                            if sum_spades_values <= 38.50:
                                                return 8.0
                                            if sum_spades_values > 38.50:
                                                return 10.0
                            if sum_spades_values > 39.50:
                                if num_nt_kings <= 0.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 42.50:
                                            if sum_spades_values <= 41.50:
                                                if sum_spades_values <= 40.50:
                                                    return 7.0
                                                if sum_spades_values > 40.50:
                                                    if num_nt_aces <= 2.50:
                                                        return 6.0
                                                    if num_nt_aces > 2.50:
                                                        return 7.0
                                            if sum_spades_values > 41.50:
                                                return 7.0
                                        if sum_spades_values > 42.50:
                                            if sum_spades_values <= 43.50:
                                                if num_nt_aces <= 2.50:
                                                    return 6.0
                                                if num_nt_aces > 2.50:
                                                    return 7.0
                                            if sum_spades_values > 43.50:
                                                if num_nt_aces <= 2.50:
                                                    return 6.0
                                                if num_nt_aces > 2.50:
                                                    return 7.0
                                    if num_void_suits > 0.50:
                                        return 7.0
                                if num_nt_kings > 0.50:
                                    if num_nt_aces <= 2.50:
                                        if num_nt_kings <= 1.50:
                                            if num_void_suits <= 0.50:
                                                return 7.0
                                            if num_void_suits > 0.50:
                                                return 8.0
                                        if num_nt_kings > 1.50:
                                            if sum_spades_values <= 41.50:
                                                if num_void_suits <= 0.50:
                                                    return 7.0
                                                if num_void_suits > 0.50:
                                                    return 8.0
                                            if sum_spades_values > 41.50:
                                                if num_nt_kings <= 2.50:
                                                    if sum_spades_values <= 44.50:
                                                        return 8.0
                                                    if sum_spades_values > 44.50:
                                                        if num_void_suits <= 0.50:
                                                            return 8.0
                                                        if num_void_suits > 0.50:
                                                            return 9.0
                                                if num_nt_kings > 2.50:
                                                    return 8.0
                                    if num_nt_aces > 2.50:
                                        if sum_spades_values <= 41.50:
                                            return 8.0
                                        if sum_spades_values > 41.50:
                                            if sum_spades_values <= 44.00:
                                                if num_nt_kings <= 2.50:
                                                    return 9.0
                                                if num_nt_kings > 2.50:
                                                    return 10.0
                                            if sum_spades_values > 44.00:
                                                return 8.0
                    if num_spades > 6.50:
                        if num_nt_aces <= 2.50:
                            if num_nt_kings <= 1.50:
                                if sum_spades_values <= 35.50:
                                    if num_void_suits <= 0.50:
                                        return 6.0
                                    if num_void_suits > 0.50:
                                        return 8.0
                                if sum_spades_values > 35.50:
                                    if sum_spades_values <= 42.50:
                                        if sum_spades_values <= 36.50:
                                            if num_void_suits <= 0.50:
                                                if num_nt_kings <= 0.50:
                                                    return 6.0
                                                if num_nt_kings > 0.50:
                                                    return 7.0
                                            if num_void_suits > 0.50:
                                                return 7.0
                                        if sum_spades_values > 36.50:
                                            if num_nt_kings <= 0.50:
                                                return 7.0
                                            if num_nt_kings > 0.50:
                                                if num_void_suits <= 0.50:
                                                    return 7.0
                                                if num_void_suits > 0.50:
                                                    return 8.0
                                    if sum_spades_values > 42.50:
                                        if sum_spades_values <= 44.50:
                                            if sum_spades_values <= 43.50:
                                                if num_void_suits <= 0.50:
                                                    return 7.0
                                                if num_void_suits > 0.50:
                                                    return 8.0
                                            if sum_spades_values > 43.50:
                                                if num_nt_kings <= 0.50:
                                                    if num_void_suits <= 0.50:
                                                        return 7.0
                                                    if num_void_suits > 0.50:
                                                        if num_spades <= 7.50:
                                                            return 7.0
                                                        if num_spades > 7.50:
                                                            return 8.0
                                                if num_nt_kings > 0.50:
                                                    return 8.0
                                        if sum_spades_values > 44.50:
                                            return 7.0
                            if num_nt_kings > 1.50:
                                if num_nt_kings <= 2.50:
                                    if num_void_suits <= 0.50:
                                        return 8.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 40.00:
                                            return 8.0
                                        if sum_spades_values > 40.00:
                                            return 9.0
                                if num_nt_kings > 2.50:
                                    if sum_spades_values <= 41.00:
                                        if sum_spades_values <= 38.50:
                                            return 6.0
                                        if sum_spades_values > 38.50:
                                            return 8.0
                                    if sum_spades_values > 41.00:
                                        return 7.0
                        if num_nt_aces > 2.50:
                            if sum_spades_values <= 37.50:
                                return 7.0
                            if sum_spades_values > 37.50:
                                if sum_spades_values <= 40.00:
                                    return 8.0
                                if sum_spades_values > 40.00:
                                    if sum_spades_values <= 44.50:
                                        if num_spades <= 7.50:
                                            if sum_spades_values <= 43.50:
                                                if num_nt_kings <= 1.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 8.0
                                                    if num_nt_kings > 0.50:
                                                        if sum_spades_values <= 42.00:
                                                            return 9.0
                                                        if sum_spades_values > 42.00:
                                                            return 8.0
                                                if num_nt_kings > 1.50:
                                                    return 9.0
                                            if sum_spades_values > 43.50:
                                                return 9.0
                                        if num_spades > 7.50:
                                            return 8.0
                                    if sum_spades_values > 44.50:
                                        return 8.0
            if sum_spades_values > 45.50:
                if num_nt_kings <= 0.50:
                    if num_void_suits <= 1.50:
                        if num_spades <= 6.50:
                            if sum_spades_values <= 47.50:
                                if num_nt_aces <= 0.50:
                                    return 5.0
                                if num_nt_aces > 0.50:
                                    return 6.0
                            if sum_spades_values > 47.50:
                                if sum_spades_values <= 48.50:
                                    if num_nt_aces <= 0.50:
                                        return 5.0
                                    if num_nt_aces > 0.50:
                                        return 7.0
                                if sum_spades_values > 48.50:
                                    if num_nt_aces <= 1.50:
                                        if sum_spades_values <= 58.50:
                                            if num_nt_aces <= 0.50:
                                                if num_void_suits <= 0.50:
                                                    if sum_spades_values <= 55.50:
                                                        return 5.0
                                                    if sum_spades_values > 55.50:
                                                        return 6.0
                                                if num_void_suits > 0.50:
                                                    return 6.0
                                            if num_nt_aces > 0.50:
                                                if num_void_suits <= 0.50:
                                                    if sum_spades_values <= 55.00:
                                                        return 6.0
                                                    if sum_spades_values > 55.00:
                                                        return 7.0
                                                if num_void_suits > 0.50:
                                                    return 7.0
                                        if sum_spades_values > 58.50:
                                            if num_nt_aces <= 0.50:
                                                return 6.0
                                            if num_nt_aces > 0.50:
                                                return 8.0
                                    if num_nt_aces > 1.50:
                                        if num_nt_aces <= 2.50:
                                            if sum_spades_values <= 56.50:
                                                if num_void_suits <= 0.50:
                                                    return 7.0
                                                if num_void_suits > 0.50:
                                                    return 8.0
                                            if sum_spades_values > 56.50:
                                                return 8.0
                                        if num_nt_aces > 2.50:
                                            return 8.0
                        if num_spades > 6.50:
                            if num_void_suits <= 0.50:
                                if sum_spades_values <= 56.50:
                                    if num_nt_aces <= 1.50:
                                        if num_spades <= 7.50:
                                            if sum_spades_values <= 54.00:
                                                if sum_spades_values <= 50.50:
                                                    if sum_spades_values <= 48.50:
                                                        return 6.0
                                                    if sum_spades_values > 48.50:
                                                        return 5.0
                                                if sum_spades_values > 50.50:
                                                    return 6.0
                                            if sum_spades_values > 54.00:
                                                if num_nt_aces <= 0.50:
                                                    return 6.0
                                                if num_nt_aces > 0.50:
                                                    return 7.0
                                        if num_spades > 7.50:
                                            if num_nt_aces <= 0.50:
                                                if num_spades <= 8.50:
                                                    return 6.0
                                                if num_spades > 8.50:
                                                    if sum_spades_values <= 54.50:
                                                        return 6.0
                                                    if sum_spades_values > 54.50:
                                                        return 7.0
                                            if num_nt_aces > 0.50:
                                                if num_spades <= 8.50:
                                                    return 7.0
                                                if num_spades > 8.50:
                                                    return 8.0
                                    if num_nt_aces > 1.50:
                                        if num_nt_aces <= 2.50:
                                            if num_spades <= 7.50:
                                                if sum_spades_values <= 51.50:
                                                    return 7.0
                                                if sum_spades_values > 51.50:
                                                    return 8.0
                                            if num_spades > 7.50:
                                                if sum_spades_values <= 47.00:
                                                    return 7.0
                                                if sum_spades_values > 47.00:
                                                    return 8.0
                                        if num_nt_aces > 2.50:
                                            if sum_spades_values <= 53.50:
                                                if sum_spades_values <= 50.00:
                                                    return 8.0
                                                if sum_spades_values > 50.00:
                                                    if num_spades <= 7.50:
                                                        if sum_spades_values <= 52.50:
                                                            return 8.0
                                                        if sum_spades_values > 52.50:
                                                            return 9.0
                                                    if num_spades > 7.50:
                                                        if sum_spades_values <= 52.00:
                                                            return 9.0
                                                        if sum_spades_values > 52.00:
                                                            return 8.0
                                            if sum_spades_values > 53.50:
                                                return 9.0
                                if sum_spades_values > 56.50:
                                    if num_nt_aces <= 1.50:
                                        if num_spades <= 7.50:
                                            if sum_spades_values <= 58.50:
                                                return 7.0
                                            if sum_spades_values > 58.50:
                                                return 6.0
                                        if num_spades > 7.50:
                                            if num_spades <= 8.50:
                                                return 8.0
                                            if num_spades > 8.50:
                                                if num_nt_aces <= 0.50:
                                                    return 7.0
                                                if num_nt_aces > 0.50:
                                                    return 8.0
                                    if num_nt_aces > 1.50:
                                        if num_nt_aces <= 2.50:
                                            if sum_spades_values <= 58.50:
                                                return 9.0
                                            if sum_spades_values > 58.50:
                                                if num_spades <= 7.50:
                                                    return 8.0
                                                if num_spades > 7.50:
                                                    return 9.0
                                        if num_nt_aces > 2.50:
                                            if sum_spades_values <= 58.50:
                                                if num_spades <= 8.50:
                                                    return 10.0
                                                if num_spades > 8.50:
                                                    return 11.0
                                            if sum_spades_values > 58.50:
                                                return 9.0
                            if num_void_suits > 0.50:
                                if num_spades <= 8.50:
                                    if sum_spades_values <= 55.50:
                                        if num_nt_aces <= 1.50:
                                            if num_nt_aces <= 0.50:
                                                if num_spades <= 7.50:
                                                    if sum_spades_values <= 54.50:
                                                        return 6.0
                                                    if sum_spades_values > 54.50:
                                                        return 7.0
                                                if num_spades > 7.50:
                                                    if sum_spades_values <= 51.50:
                                                        return 6.0
                                                    if sum_spades_values > 51.50:
                                                        return 7.0
                                            if num_nt_aces > 0.50:
                                                if sum_spades_values <= 52.00:
                                                    return 7.0
                                                if sum_spades_values > 52.00:
                                                    if sum_spades_values <= 53.50:
                                                        if num_spades <= 7.50:
                                                            return 7.0
                                                        if num_spades > 7.50:
                                                            return 8.0
                                                    if sum_spades_values > 53.50:
                                                        return 8.0
                                        if num_nt_aces > 1.50:
                                            if sum_spades_values <= 54.50:
                                                return 8.0
                                            if sum_spades_values > 54.50:
                                                return 9.0
                                    if sum_spades_values > 55.50:
                                        if num_nt_aces <= 1.50:
                                            if num_spades <= 7.50:
                                                return 7.0
                                            if num_spades > 7.50:
                                                if num_nt_aces <= 0.50:
                                                    return 7.0
                                                if num_nt_aces > 0.50:
                                                    return 8.0
                                        if num_nt_aces > 1.50:
                                            return 9.0
                                if num_spades > 8.50:
                                    if num_nt_aces <= 0.50:
                                        return 7.0
                                    if num_nt_aces > 0.50:
                                        if sum_spades_values <= 56.00:
                                            if num_nt_aces <= 1.50:
                                                return 8.0
                                            if num_nt_aces > 1.50:
                                                return 9.0
                                        if sum_spades_values > 56.00:
                                            if num_nt_aces <= 1.50:
                                                return 8.0
                                            if num_nt_aces > 1.50:
                                                return 10.0
                    if num_void_suits > 1.50:
                        if num_nt_aces <= 0.50:
                            if num_spades <= 8.50:
                                if sum_spades_values <= 58.50:
                                    return 8.0
                                if sum_spades_values > 58.50:
                                    if num_spades <= 7.50:
                                        return 8.0
                                    if num_spades > 7.50:
                                        return 9.0
                            if num_spades > 8.50:
                                return 9.0
                        if num_nt_aces > 0.50:
                            if num_spades <= 6.50:
                                if sum_spades_values <= 54.00:
                                    return 8.0
                                if sum_spades_values > 54.00:
                                    return 9.0
                            if num_spades > 6.50:
                                return 9.0
                if num_nt_kings > 0.50:
                    if sum_spades_values <= 50.50:
                        if num_void_suits <= 0.50:
                            if sum_spades_values <= 47.50:
                                if num_nt_kings <= 1.50:
                                    if num_nt_aces <= 1.50:
                                        if num_spades <= 6.50:
                                            if num_nt_aces <= 0.50:
                                                return 5.0
                                            if num_nt_aces > 0.50:
                                                return 6.0
                                        if num_spades > 6.50:
                                            if num_spades <= 7.50:
                                                return 6.0
                                            if num_spades > 7.50:
                                                if sum_spades_values <= 46.50:
                                                    return 6.0
                                                if sum_spades_values > 46.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 6.0
                                                    if num_nt_aces > 0.50:
                                                        return 7.0
                                    if num_nt_aces > 1.50:
                                        if num_spades <= 6.50:
                                            if num_nt_aces <= 2.50:
                                                return 7.0
                                            if num_nt_aces > 2.50:
                                                return 8.0
                                        if num_spades > 6.50:
                                            return 9.0
                                if num_nt_kings > 1.50:
                                    if sum_spades_values <= 46.50:
                                        if num_nt_aces <= 2.50:
                                            if num_nt_kings <= 2.50:
                                                if num_spades <= 6.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 6.0
                                                    if num_nt_aces > 0.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 7.0
                                                        if num_nt_aces > 1.50:
                                                            return 8.0
                                                if num_spades > 6.50:
                                                    if num_spades <= 7.50:
                                                        return 7.0
                                                    if num_spades > 7.50:
                                                        if num_nt_aces <= 1.50:
                                                            if num_nt_aces <= 0.50:
                                                                return 7.0
                                                            if num_nt_aces > 0.50:
                                                                return 8.0
                                                        if num_nt_aces > 1.50:
                                                            return 7.0
                                            if num_nt_kings > 2.50:
                                                if num_nt_aces <= 1.50:
                                                    if num_spades <= 7.50:
                                                        return 7.0
                                                    if num_spades > 7.50:
                                                        return 8.0
                                                if num_nt_aces > 1.50:
                                                    return 8.0
                                        if num_nt_aces > 2.50:
                                            return 11.0
                                    if sum_spades_values > 46.50:
                                        if num_nt_kings <= 2.50:
                                            if num_nt_aces <= 1.50:
                                                if num_nt_aces <= 0.50:
                                                    if num_spades <= 7.50:
                                                        return 6.0
                                                    if num_spades > 7.50:
                                                        return 7.0
                                                if num_nt_aces > 0.50:
                                                    return 8.0
                                            if num_nt_aces > 1.50:
                                                if num_nt_aces <= 2.50:
                                                    return 10.0
                                                if num_nt_aces > 2.50:
                                                    if num_spades <= 6.50:
                                                        return 9.0
                                                    if num_spades > 6.50:
                                                        return 10.0
                                        if num_nt_kings > 2.50:
                                            if num_nt_aces <= 1.50:
                                                if num_spades <= 6.50:
                                                    return 7.0
                                                if num_spades > 6.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 7.0
                                                    if num_nt_aces > 0.50:
                                                        return 8.0
                                            if num_nt_aces > 1.50:
                                                if num_spades <= 6.50:
                                                    return 10.0
                                                if num_spades > 6.50:
                                                    return 9.0
                            if sum_spades_values > 47.50:
                                if sum_spades_values <= 49.50:
                                    if num_nt_kings <= 1.50:
                                        if num_nt_aces <= 1.50:
                                            return 6.0
                                        if num_nt_aces > 1.50:
                                            return 8.0
                                    if num_nt_kings > 1.50:
                                        if num_nt_aces <= 0.50:
                                            if num_nt_kings <= 2.50:
                                                if num_spades <= 7.00:
                                                    return 6.0
                                                if num_spades > 7.00:
                                                    return 7.0
                                            if num_nt_kings > 2.50:
                                                return 6.0
                                        if num_nt_aces > 0.50:
                                            if num_nt_kings <= 2.50:
                                                if sum_spades_values <= 48.50:
                                                    if num_spades <= 7.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 7.0
                                                        if num_nt_aces > 1.50:
                                                            return 8.0
                                                    if num_spades > 7.50:
                                                        if num_nt_aces <= 2.50:
                                                            return 8.0
                                                        if num_nt_aces > 2.50:
                                                            return 10.0
                                                if sum_spades_values > 48.50:
                                                    if num_spades <= 7.50:
                                                        if num_spades <= 6.50:
                                                            if num_nt_aces <= 2.50:
                                                                return 8.0
                                                            if num_nt_aces > 2.50:
                                                                return 9.0
                                                        if num_spades > 6.50:
                                                            if num_nt_aces <= 2.00:
                                                                return 7.0
                                                            if num_nt_aces > 2.00:
                                                                return 10.0
                                                    if num_spades > 7.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 8.0
                                                        if num_nt_aces > 1.50:
                                                            return 9.0
                                            if num_nt_kings > 2.50:
                                                if num_nt_aces <= 2.50:
                                                    if sum_spades_values <= 48.50:
                                                        if num_spades <= 6.50:
                                                            return 8.0
                                                        if num_spades > 6.50:
                                                            return 9.0
                                                    if sum_spades_values > 48.50:
                                                        return 8.0
                                                if num_nt_aces > 2.50:
                                                    if num_spades <= 6.50:
                                                        if sum_spades_values <= 48.50:
                                                            return 9.0
                                                        if sum_spades_values > 48.50:
                                                            return 10.0
                                                    if num_spades > 6.50:
                                                        return 11.0
                                if sum_spades_values > 49.50:
                                    if num_spades <= 7.50:
                                        if num_nt_kings <= 1.50:
                                            if num_nt_aces <= 1.50:
                                                if num_spades <= 6.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 6.0
                                                    if num_nt_aces > 0.50:
                                                        return 7.0
                                                if num_spades > 6.50:
                                                    return 6.0
                                            if num_nt_aces > 1.50:
                                                return 8.0
                                        if num_nt_kings > 1.50:
                                            if num_nt_aces <= 0.50:
                                                return 7.0
                                            if num_nt_aces > 0.50:
                                                if num_spades <= 6.50:
                                                    if num_nt_aces <= 2.00:
                                                        return 8.0
                                                    if num_nt_aces > 2.00:
                                                        return 10.0
                                                if num_spades > 6.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 9.0
                                                    if num_nt_kings > 2.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 8.0
                                                        if num_nt_aces > 1.50:
                                                            return 10.0
                                    if num_spades > 7.50:
                                        if num_nt_kings <= 1.50:
                                            if num_nt_aces <= 0.50:
                                                return 6.0
                                            if num_nt_aces > 0.50:
                                                return 8.0
                                        if num_nt_kings > 1.50:
                                            if num_nt_aces <= 1.50:
                                                if num_nt_aces <= 0.50:
                                                    return 7.0
                                                if num_nt_aces > 0.50:
                                                    return 8.0
                                            if num_nt_aces > 1.50:
                                                return 9.0
                        if num_void_suits > 0.50:
                            if num_nt_aces <= 0.50:
                                if num_spades <= 6.50:
                                    if num_nt_kings <= 1.50:
                                        if num_void_suits <= 1.50:
                                            return 6.0
                                        if num_void_suits > 1.50:
                                            if sum_spades_values <= 47.00:
                                                return 7.0
                                            if sum_spades_values > 47.00:
                                                return 8.0
                                    if num_nt_kings > 1.50:
                                        return 7.0
                                if num_spades > 6.50:
                                    if num_nt_kings <= 1.50:
                                        if num_void_suits <= 1.50:
                                            return 7.0
                                        if num_void_suits > 1.50:
                                            if sum_spades_values <= 47.50:
                                                if sum_spades_values <= 46.50:
                                                    return 8.0
                                                if sum_spades_values > 46.50:
                                                    if num_spades <= 7.50:
                                                        return 8.0
                                                    if num_spades > 7.50:
                                                        return 9.0
                                            if sum_spades_values > 47.50:
                                                return 8.0
                                    if num_nt_kings > 1.50:
                                        if num_spades <= 7.50:
                                            return 7.0
                                        if num_spades > 7.50:
                                            if sum_spades_values <= 49.50:
                                                if sum_spades_values <= 47.00:
                                                    return 7.0
                                                if sum_spades_values > 47.00:
                                                    return 8.0
                                            if sum_spades_values > 49.50:
                                                return 7.0
                            if num_nt_aces > 0.50:
                                if num_void_suits <= 1.50:
                                    if num_nt_kings <= 1.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 48.50:
                                                if num_nt_aces <= 1.50:
                                                    return 7.0
                                                if num_nt_aces > 1.50:
                                                    return 8.0
                                            if sum_spades_values > 48.50:
                                                if sum_spades_values <= 49.50:
                                                    return 7.0
                                                if sum_spades_values > 49.50:
                                                    if num_nt_aces <= 1.50:
                                                        return 7.0
                                                    if num_nt_aces > 1.50:
                                                        return 8.0
                                        if num_spades > 6.50:
                                            if num_nt_aces <= 1.50:
                                                return 8.0
                                            if num_nt_aces > 1.50:
                                                if num_spades <= 7.50:
                                                    if sum_spades_values <= 48.00:
                                                        return 8.0
                                                    if sum_spades_values > 48.00:
                                                        return 9.0
                                                if num_spades > 7.50:
                                                    return 9.0
                                    if num_nt_kings > 1.50:
                                        if num_nt_aces <= 1.50:
                                            if num_spades <= 7.50:
                                                return 8.0
                                            if num_spades > 7.50:
                                                if sum_spades_values <= 47.50:
                                                    if sum_spades_values <= 46.50:
                                                        return 8.0
                                                    if sum_spades_values > 46.50:
                                                        return 9.0
                                                if sum_spades_values > 47.50:
                                                    return 8.0
                                        if num_nt_aces > 1.50:
                                            return 9.0
                                if num_void_suits > 1.50:
                                    if num_spades <= 6.50:
                                        return 8.0
                                    if num_spades > 6.50:
                                        if num_spades <= 7.50:
                                            return 9.0
                                        if num_spades > 7.50:
                                            if sum_spades_values <= 47.50:
                                                return 9.0
                                            if sum_spades_values > 47.50:
                                                if sum_spades_values <= 49.00:
                                                    return 10.0
                                                if sum_spades_values > 49.00:
                                                    return 9.0
                    if sum_spades_values > 50.50:
                        if num_void_suits <= 1.50:
                            if num_spades <= 8.50:
                                if num_void_suits <= 0.50:
                                    if num_nt_aces <= 0.50:
                                        if num_nt_kings <= 2.50:
                                            if sum_spades_values <= 54.50:
                                                if num_nt_kings <= 1.50:
                                                    if sum_spades_values <= 52.50:
                                                        return 7.0
                                                    if sum_spades_values > 52.50:
                                                        return 6.0
                                                if num_nt_kings > 1.50:
                                                    if sum_spades_values <= 52.00:
                                                        return 7.0
                                                    if sum_spades_values > 52.00:
                                                        return 6.0
                                            if sum_spades_values > 54.50:
                                                if sum_spades_values <= 57.50:
                                                    if num_nt_kings <= 1.50:
                                                        if sum_spades_values <= 56.50:
                                                            if num_spades <= 6.50:
                                                                return 6.0
                                                            if num_spades > 6.50:
                                                                return 7.0
                                                        if sum_spades_values > 56.50:
                                                            if num_spades <= 6.50:
                                                                return 6.0
                                                            if num_spades > 6.50:
                                                                return 7.0
                                                    if num_nt_kings > 1.50:
                                                        return 7.0
                                                if sum_spades_values > 57.50:
                                                    return 7.0
                                        if num_nt_kings > 2.50:
                                            if sum_spades_values <= 55.50:
                                                return 7.0
                                            if sum_spades_values > 55.50:
                                                if num_spades <= 6.50:
                                                    return 7.0
                                                if num_spades > 6.50:
                                                    return 8.0
                                    if num_nt_aces > 0.50:
                                        if num_nt_aces <= 2.50:
                                            if num_spades <= 6.50:
                                                if num_nt_kings <= 1.50:
                                                    if sum_spades_values <= 51.50:
                                                        return 8.0
                                                    if sum_spades_values > 51.50:
                                                        if sum_spades_values <= 58.50:
                                                            if num_nt_aces <= 1.50:
                                                                return 7.0
                                                            if num_nt_aces > 1.50:
                                                                return 8.0
                                                        if sum_spades_values > 58.50:
                                                            return 8.0
                                                if num_nt_kings > 1.50:
                                                    if num_nt_kings <= 2.50:
                                                        if num_nt_aces <= 1.50:
                                                            if sum_spades_values <= 54.50:
                                                                return 7.0
                                                            if sum_spades_values > 54.50:
                                                                return 8.0
                                                        if num_nt_aces > 1.50:
                                                            if sum_spades_values <= 55.00:
                                                                return 8.0
                                                            if sum_spades_values > 55.00:
                                                                return 9.0
                                                    if num_nt_kings > 2.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 8.0
                                                        if num_nt_aces > 1.50:
                                                            return 9.0
                                            if num_spades > 6.50:
                                                if num_nt_aces <= 1.50:
                                                    if sum_spades_values <= 55.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 7.0
                                                        if num_nt_kings > 1.50:
                                                            if sum_spades_values <= 51.50:
                                                                if num_spades <= 7.50:
                                                                    return 8.0
                                                                if num_spades > 7.50:
                                                                    return 9.0
                                                            if sum_spades_values > 51.50:
                                                                return 8.0
                                                    if sum_spades_values > 55.50:
                                                        if num_nt_kings <= 2.50:
                                                            if num_spades <= 7.50:
                                                                return 8.0
                                                            if num_spades > 7.50:
                                                                if sum_spades_values <= 57.50:
                                                                    return 8.0
                                                                if sum_spades_values > 57.50:
                                                                    if sum_spades_values <= 58.50:
                                                                        return 9.0
                                                                    if sum_spades_values > 58.50:
                                                                        return 8.0
                                                        if num_nt_kings > 2.50:
                                                            return 9.0
                                                if num_nt_aces > 1.50:
                                                    if num_nt_kings <= 1.50:
                                                        if sum_spades_values <= 54.00:
                                                            return 8.0
                                                        if sum_spades_values > 54.00:
                                                            return 9.0
                                                    if num_nt_kings > 1.50:
                                                        if sum_spades_values <= 56.50:
                                                            if sum_spades_values <= 53.50:
                                                                return 9.0
                                                            if sum_spades_values > 53.50:
                                                                if sum_spades_values <= 55.50:
                                                                    if num_nt_kings <= 2.50:
                                                                        return 9.0
                                                                    if num_nt_kings > 2.50:
                                                                        return 10.0
                                                                if sum_spades_values > 55.50:
                                                                    return 9.0
                                                        if sum_spades_values > 56.50:
                                                            if sum_spades_values <= 58.00:
                                                                if num_nt_kings <= 2.50:
                                                                    return 9.0
                                                                if num_nt_kings > 2.50:
                                                                    return 10.0
                                                            if sum_spades_values > 58.00:
                                                                return 9.0
                                        if num_nt_aces > 2.50:
                                            if num_nt_kings <= 1.50:
                                                if num_spades <= 6.50:
                                                    return 9.0
                                                if num_spades > 6.50:
                                                    if sum_spades_values <= 52.50:
                                                        return 9.0
                                                    if sum_spades_values > 52.50:
                                                        if sum_spades_values <= 53.50:
                                                            return 11.0
                                                        if sum_spades_values > 53.50:
                                                            if sum_spades_values <= 55.50:
                                                                return 10.0
                                                            if sum_spades_values > 55.50:
                                                                if num_spades <= 7.50:
                                                                    return 10.0
                                                                if num_spades > 7.50:
                                                                    if sum_spades_values <= 58.00:
                                                                        if sum_spades_values <= 56.50:
                                                                            return 11.0
                                                                        if sum_spades_values > 56.50:
                                                                            return 10.0
                                                                    if sum_spades_values > 58.00:
                                                                        return 11.0
                                            if num_nt_kings > 1.50:
                                                if num_nt_kings <= 2.50:
                                                    if sum_spades_values <= 57.00:
                                                        return 10.0
                                                    if sum_spades_values > 57.00:
                                                        return 11.0
                                                if num_nt_kings > 2.50:
                                                    if sum_spades_values <= 58.50:
                                                        if sum_spades_values <= 52.00:
                                                            return 11.0
                                                        if sum_spades_values > 52.00:
                                                            if num_spades <= 6.50:
                                                                if sum_spades_values <= 53.50:
                                                                    return 10.0
                                                                if sum_spades_values > 53.50:
                                                                    if sum_spades_values <= 55.00:
                                                                        return 11.0
                                                                    if sum_spades_values > 55.00:
                                                                        return 10.0
                                                            if num_spades > 6.50:
                                                                return 10.0
                                                    if sum_spades_values > 58.50:
                                                        return 11.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 58.50:
                                        if num_nt_aces <= 1.50:
                                            if num_nt_aces <= 0.50:
                                                if num_spades <= 6.50:
                                                    if num_nt_kings <= 1.50:
                                                        if sum_spades_values <= 52.50:
                                                            return 6.0
                                                        if sum_spades_values > 52.50:
                                                            return 7.0
                                                    if num_nt_kings > 1.50:
                                                        if sum_spades_values <= 56.00:
                                                            return 7.0
                                                        if sum_spades_values > 56.00:
                                                            return 8.0
                                                if num_spades > 6.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_spades <= 7.50:
                                                            return 7.0
                                                        if num_spades > 7.50:
                                                            if sum_spades_values <= 54.00:
                                                                return 7.0
                                                            if sum_spades_values > 54.00:
                                                                return 8.0
                                                    if num_nt_kings > 1.50:
                                                        return 8.0
                                            if num_nt_aces > 0.50:
                                                if num_spades <= 7.50:
                                                    if sum_spades_values <= 57.50:
                                                        if num_spades <= 6.50:
                                                            if num_nt_kings <= 1.50:
                                                                if sum_spades_values <= 53.00:
                                                                    return 7.0
                                                                if sum_spades_values > 53.00:
                                                                    return 8.0
                                                            if num_nt_kings > 1.50:
                                                                return 8.0
                                                        if num_spades > 6.50:
                                                            if sum_spades_values <= 52.50:
                                                                return 8.0
                                                            if sum_spades_values > 52.50:
                                                                if num_nt_kings <= 1.50:
                                                                    return 8.0
                                                                if num_nt_kings > 1.50:
                                                                    return 9.0
                                                    if sum_spades_values > 57.50:
                                                        if num_spades <= 6.50:
                                                            return 9.0
                                                        if num_spades > 6.50:
                                                            return 8.0
                                                if num_spades > 7.50:
                                                    if sum_spades_values <= 54.50:
                                                        if sum_spades_values <= 51.50:
                                                            if num_nt_kings <= 1.50:
                                                                return 8.0
                                                            if num_nt_kings > 1.50:
                                                                return 9.0
                                                        if sum_spades_values > 51.50:
                                                            if num_nt_kings <= 1.50:
                                                                return 8.0
                                                            if num_nt_kings > 1.50:
                                                                return 9.0
                                                    if sum_spades_values > 54.50:
                                                        return 9.0
                                        if num_nt_aces > 1.50:
                                            if num_spades <= 6.50:
                                                if sum_spades_values <= 56.00:
                                                    return 9.0
                                                if sum_spades_values > 56.00:
                                                    if sum_spades_values <= 57.50:
                                                        return 10.0
                                                    if sum_spades_values > 57.50:
                                                        return 9.0
                                            if num_spades > 6.50:
                                                if num_spades <= 7.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 9.0
                                                    if num_nt_kings > 1.50:
                                                        if sum_spades_values <= 51.50:
                                                            return 9.0
                                                        if sum_spades_values > 51.50:
                                                            return 10.0
                                                if num_spades > 7.50:
                                                    if sum_spades_values <= 54.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 9.0
                                                        if num_nt_kings > 1.50:
                                                            if sum_spades_values <= 53.50:
                                                                return 10.0
                                                            if sum_spades_values > 53.50:
                                                                return 9.0
                                                    if sum_spades_values > 54.50:
                                                        return 10.0
                                    if sum_spades_values > 58.50:
                                        if num_nt_aces <= 0.50:
                                            return 8.0
                                        if num_nt_aces > 0.50:
                                            if num_spades <= 7.50:
                                                if num_spades <= 6.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 8.0
                                                        if num_nt_aces > 1.50:
                                                            return 9.0
                                                    if num_nt_kings > 1.50:
                                                        return 9.0
                                                if num_spades > 6.50:
                                                    return 9.0
                                            if num_spades > 7.50:
                                                if num_nt_aces <= 1.50:
                                                    return 9.0
                                                if num_nt_aces > 1.50:
                                                    return 10.0
                            if num_spades > 8.50:
                                if num_nt_aces <= 0.50:
                                    if sum_spades_values <= 55.00:
                                        if num_void_suits <= 0.50:
                                            return 6.0
                                        if num_void_suits > 0.50:
                                            return 8.0
                                    if sum_spades_values > 55.00:
                                        return 8.0
                                if num_nt_aces > 0.50:
                                    if num_nt_aces <= 1.50:
                                        if sum_spades_values <= 56.50:
                                            if num_nt_kings <= 1.50:
                                                return 8.0
                                            if num_nt_kings > 1.50:
                                                return 9.0
                                        if sum_spades_values > 56.50:
                                            if num_void_suits <= 0.50:
                                                if num_nt_kings <= 1.50:
                                                    return 9.0
                                                if num_nt_kings > 1.50:
                                                    if sum_spades_values <= 57.50:
                                                        return 10.0
                                                    if sum_spades_values > 57.50:
                                                        return 9.0
                                            if num_void_suits > 0.50:
                                                return 9.0
                                    if num_nt_aces > 1.50:
                                        if sum_spades_values <= 55.50:
                                            return 10.0
                                        if sum_spades_values > 55.50:
                                            return 9.0
                        if num_void_suits > 1.50:
                            if num_spades <= 8.50:
                                if num_nt_aces <= 0.50:
                                    if sum_spades_values <= 52.50:
                                        return 8.0
                                    if sum_spades_values > 52.50:
                                        if sum_spades_values <= 55.50:
                                            if sum_spades_values <= 54.00:
                                                if num_spades <= 7.00:
                                                    return 8.0
                                                if num_spades > 7.00:
                                                    return 9.0
                                            if sum_spades_values > 54.00:
                                                return 9.0
                                        if sum_spades_values > 55.50:
                                            if sum_spades_values <= 56.50:
                                                if num_spades <= 7.00:
                                                    return 8.0
                                                if num_spades > 7.00:
                                                    return 9.0
                                            if sum_spades_values > 56.50:
                                                if sum_spades_values <= 58.00:
                                                    return 9.0
                                                if sum_spades_values > 58.00:
                                                    if num_spades <= 7.00:
                                                        return 8.0
                                                    if num_spades > 7.00:
                                                        return 9.0
                                if num_nt_aces > 0.50:
                                    if num_spades <= 7.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 52.50:
                                                return 8.0
                                            if sum_spades_values > 52.50:
                                                return 9.0
                                        if num_spades > 6.50:
                                            return 9.0
                                    if num_spades > 7.50:
                                        if sum_spades_values <= 53.50:
                                            return 9.0
                                        if sum_spades_values > 53.50:
                                            if sum_spades_values <= 56.50:
                                                if sum_spades_values <= 55.00:
                                                    return 10.0
                                                if sum_spades_values > 55.00:
                                                    return 9.0
                                            if sum_spades_values > 56.50:
                                                return 10.0
                            if num_spades > 8.50:
                                return 10.0
        if sum_spades_values > 59.50:
            if sum_spades_values <= 69.50:
                if num_nt_aces <= 1.50:
                    if num_spades <= 8.50:
                        if num_void_suits <= 1.50:
                            if num_nt_kings <= 1.50:
                                if num_void_suits <= 0.50:
                                    if num_nt_aces <= 0.50:
                                        if num_spades <= 7.50:
                                            if num_spades <= 6.50:
                                                if num_nt_kings <= 0.50:
                                                    return 6.0
                                                if num_nt_kings > 0.50:
                                                    return 7.0
                                            if num_spades > 6.50:
                                                if sum_spades_values <= 62.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 6.0
                                                    if num_nt_kings > 0.50:
                                                        return 7.0
                                                if sum_spades_values > 62.50:
                                                    if sum_spades_values <= 67.00:
                                                        return 7.0
                                                    if sum_spades_values > 67.00:
                                                        if sum_spades_values <= 68.50:
                                                            return 8.0
                                                        if sum_spades_values > 68.50:
                                                            return 7.0
                                        if num_spades > 7.50:
                                            if sum_spades_values <= 61.50:
                                                return 7.0
                                            if sum_spades_values > 61.50:
                                                if sum_spades_values <= 67.50:
                                                    if sum_spades_values <= 65.50:
                                                        if num_nt_kings <= 0.50:
                                                            return 7.0
                                                        if num_nt_kings > 0.50:
                                                            return 8.0
                                                    if sum_spades_values > 65.50:
                                                        if sum_spades_values <= 66.50:
                                                            if num_nt_kings <= 0.50:
                                                                return 7.0
                                                            if num_nt_kings > 0.50:
                                                                return 8.0
                                                        if sum_spades_values > 66.50:
                                                            if num_nt_kings <= 0.50:
                                                                return 7.0
                                                            if num_nt_kings > 0.50:
                                                                return 8.0
                                                if sum_spades_values > 67.50:
                                                    return 8.0
                                    if num_nt_aces > 0.50:
                                        if sum_spades_values <= 61.50:
                                            if num_nt_kings <= 0.50:
                                                return 7.0
                                            if num_nt_kings > 0.50:
                                                return 8.0
                                        if sum_spades_values > 61.50:
                                            if num_spades <= 7.50:
                                                if num_nt_kings <= 0.50:
                                                    if sum_spades_values <= 66.50:
                                                        if sum_spades_values <= 64.50:
                                                            return 7.0
                                                        if sum_spades_values > 64.50:
                                                            if num_spades <= 6.50:
                                                                return 7.0
                                                            if num_spades > 6.50:
                                                                return 8.0
                                                    if sum_spades_values > 66.50:
                                                        return 8.0
                                                if num_nt_kings > 0.50:
                                                    if num_spades <= 6.50:
                                                        return 8.0
                                                    if num_spades > 6.50:
                                                        if sum_spades_values <= 66.00:
                                                            return 8.0
                                                        if sum_spades_values > 66.00:
                                                            return 9.0
                                            if num_spades > 7.50:
                                                if num_nt_kings <= 0.50:
                                                    if sum_spades_values <= 67.00:
                                                        return 8.0
                                                    if sum_spades_values > 67.00:
                                                        return 9.0
                                                if num_nt_kings > 0.50:
                                                    return 9.0
                                if num_void_suits > 0.50:
                                    if num_nt_kings <= 0.50:
                                        if num_nt_aces <= 0.50:
                                            if sum_spades_values <= 65.50:
                                                if num_spades <= 7.50:
                                                    return 7.0
                                                if num_spades > 7.50:
                                                    if sum_spades_values <= 62.00:
                                                        return 7.0
                                                    if sum_spades_values > 62.00:
                                                        return 8.0
                                            if sum_spades_values > 65.50:
                                                if num_spades <= 6.50:
                                                    return 7.0
                                                if num_spades > 6.50:
                                                    return 8.0
                                        if num_nt_aces > 0.50:
                                            if num_spades <= 6.50:
                                                return 8.0
                                            if num_spades > 6.50:
                                                if sum_spades_values <= 65.00:
                                                    return 8.0
                                                if sum_spades_values > 65.00:
                                                    return 9.0
                                    if num_nt_kings > 0.50:
                                        if num_nt_aces <= 0.50:
                                            if num_spades <= 6.50:
                                                if sum_spades_values <= 63.50:
                                                    return 7.0
                                                if sum_spades_values > 63.50:
                                                    return 8.0
                                            if num_spades > 6.50:
                                                if sum_spades_values <= 67.00:
                                                    return 8.0
                                                if sum_spades_values > 67.00:
                                                    if num_spades <= 7.50:
                                                        return 8.0
                                                    if num_spades > 7.50:
                                                        return 9.0
                                        if num_nt_aces > 0.50:
                                            if sum_spades_values <= 64.50:
                                                if num_spades <= 6.50:
                                                    return 8.0
                                                if num_spades > 6.50:
                                                    return 9.0
                                            if sum_spades_values > 64.50:
                                                return 9.0
                            if num_nt_kings > 1.50:
                                if num_spades <= 6.50:
                                    if num_nt_aces <= 0.50:
                                        if sum_spades_values <= 65.50:
                                            if sum_spades_values <= 64.00:
                                                if num_nt_kings <= 2.50:
                                                    if num_void_suits <= 0.50:
                                                        return 7.0
                                                    if num_void_suits > 0.50:
                                                        return 8.0
                                                if num_nt_kings > 2.50:
                                                    return 8.0
                                            if sum_spades_values > 64.00:
                                                return 7.0
                                        if sum_spades_values > 65.50:
                                            return 8.0
                                    if num_nt_aces > 0.50:
                                        if sum_spades_values <= 62.50:
                                            if num_void_suits <= 0.50:
                                                if sum_spades_values <= 61.50:
                                                    if num_nt_kings <= 2.50:
                                                        return 8.0
                                                    if num_nt_kings > 2.50:
                                                        return 9.0
                                                if sum_spades_values > 61.50:
                                                    return 8.0
                                            if num_void_suits > 0.50:
                                                return 9.0
                                        if sum_spades_values > 62.50:
                                            return 9.0
                                if num_spades > 6.50:
                                    if sum_spades_values <= 64.50:
                                        if num_nt_aces <= 0.50:
                                            if num_spades <= 7.50:
                                                if num_void_suits <= 0.50:
                                                    return 8.0
                                                if num_void_suits > 0.50:
                                                    if sum_spades_values <= 63.50:
                                                        return 8.0
                                                    if sum_spades_values > 63.50:
                                                        return 9.0
                                            if num_spades > 7.50:
                                                if num_void_suits <= 0.50:
                                                    return 8.0
                                                if num_void_suits > 0.50:
                                                    return 9.0
                                        if num_nt_aces > 0.50:
                                            if sum_spades_values <= 63.50:
                                                return 9.0
                                            if sum_spades_values > 63.50:
                                                return 10.0
                                    if sum_spades_values > 64.50:
                                        if num_void_suits <= 0.50:
                                            if num_nt_aces <= 0.50:
                                                if num_nt_kings <= 2.50:
                                                    return 8.0
                                                if num_nt_kings > 2.50:
                                                    if sum_spades_values <= 66.50:
                                                        return 8.0
                                                    if sum_spades_values > 66.50:
                                                        return 9.0
                                            if num_nt_aces > 0.50:
                                                if sum_spades_values <= 67.50:
                                                    if sum_spades_values <= 65.50:
                                                        if num_spades <= 7.50:
                                                            return 9.0
                                                        if num_spades > 7.50:
                                                            if num_nt_kings <= 2.50:
                                                                return 9.0
                                                            if num_nt_kings > 2.50:
                                                                return 10.0
                                                    if sum_spades_values > 65.50:
                                                        if num_spades <= 7.50:
                                                            return 9.0
                                                        if num_spades > 7.50:
                                                            if num_nt_kings <= 2.50:
                                                                return 9.0
                                                            if num_nt_kings > 2.50:
                                                                return 10.0
                                                if sum_spades_values > 67.50:
                                                    if num_spades <= 7.50:
                                                        return 9.0
                                                    if num_spades > 7.50:
                                                        if num_nt_kings <= 2.50:
                                                            return 10.0
                                                        if num_nt_kings > 2.50:
                                                            if sum_spades_values <= 68.50:
                                                                return 10.0
                                                            if sum_spades_values > 68.50:
                                                                return 11.0
                                        if num_void_suits > 0.50:
                                            if num_spades <= 7.50:
                                                if num_nt_aces <= 0.50:
                                                    return 9.0
                                                if num_nt_aces > 0.50:
                                                    return 10.0
                                            if num_spades > 7.50:
                                                if sum_spades_values <= 66.50:
                                                    return 10.0
                                                if sum_spades_values > 66.50:
                                                    if num_nt_aces <= 0.50:
                                                        return 9.0
                                                    if num_nt_aces > 0.50:
                                                        return 10.0
                        if num_void_suits > 1.50:
                            if num_spades <= 6.50:
                                if sum_spades_values <= 67.50:
                                    if sum_spades_values <= 64.50:
                                        if sum_spades_values <= 61.50:
                                            if num_nt_aces <= 0.50:
                                                if sum_spades_values <= 60.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 9.0
                                                    if num_nt_kings > 0.50:
                                                        return 8.0
                                                if sum_spades_values > 60.50:
                                                    return 9.0
                                            if num_nt_aces > 0.50:
                                                return 8.0
                                        if sum_spades_values > 61.50:
                                            if num_nt_kings <= 0.50:
                                                return 9.0
                                            if num_nt_kings > 0.50:
                                                if sum_spades_values <= 63.50:
                                                    if sum_spades_values <= 62.50:
                                                        if num_nt_aces <= 0.50:
                                                            return 9.0
                                                        if num_nt_aces > 0.50:
                                                            return 8.0
                                                    if sum_spades_values > 62.50:
                                                        if num_nt_aces <= 0.50:
                                                            return 8.0
                                                        if num_nt_aces > 0.50:
                                                            return 9.0
                                                if sum_spades_values > 63.50:
                                                    return 8.0
                                    if sum_spades_values > 64.50:
                                        if sum_spades_values <= 66.50:
                                            if num_nt_aces <= 0.50:
                                                return 7.0
                                            if num_nt_aces > 0.50:
                                                if sum_spades_values <= 65.50:
                                                    return 8.0
                                                if sum_spades_values > 65.50:
                                                    return 7.0
                                        if sum_spades_values > 66.50:
                                            return 9.0
                                if sum_spades_values > 67.50:
                                    return 8.0
                            if num_spades > 6.50:
                                if sum_spades_values <= 66.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 7.50:
                                            if num_nt_aces <= 0.50:
                                                return 9.0
                                            if num_nt_aces > 0.50:
                                                return 10.0
                                        if num_spades > 7.50:
                                            if sum_spades_values <= 61.00:
                                                if num_nt_aces <= 0.50:
                                                    return 8.0
                                                if num_nt_aces > 0.50:
                                                    return 10.0
                                            if sum_spades_values > 61.00:
                                                if num_nt_aces <= 0.50:
                                                    return 9.0
                                                if num_nt_aces > 0.50:
                                                    return 10.0
                                    if num_nt_kings > 0.50:
                                        if num_spades <= 7.50:
                                            if num_nt_aces <= 0.50:
                                                return 9.0
                                            if num_nt_aces > 0.50:
                                                return 10.0
                                        if num_spades > 7.50:
                                            if sum_spades_values <= 60.50:
                                                return 9.0
                                            if sum_spades_values > 60.50:
                                                if num_nt_aces <= 0.50:
                                                    return 9.0
                                                if num_nt_aces > 0.50:
                                                    return 10.0
                                if sum_spades_values > 66.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 7.50:
                                            if sum_spades_values <= 67.50:
                                                return 10.0
                                            if sum_spades_values > 67.50:
                                                if num_nt_aces <= 0.50:
                                                    return 9.0
                                                if num_nt_aces > 0.50:
                                                    return 11.0
                                        if num_spades > 7.50:
                                            if num_nt_aces <= 0.50:
                                                if sum_spades_values <= 67.50:
                                                    return 9.0
                                                if sum_spades_values > 67.50:
                                                    return 10.0
                                            if num_nt_aces > 0.50:
                                                return 11.0
                                    if num_nt_kings > 0.50:
                                        return 10.0
                    if num_spades > 8.50:
                        if num_nt_aces <= 0.50:
                            if sum_spades_values <= 66.50:
                                if sum_spades_values <= 61.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_kings <= 1.00:
                                            return 7.0
                                        if num_nt_kings > 1.00:
                                            return 8.0
                                    if num_void_suits > 0.50:
                                        return 8.0
                                if sum_spades_values > 61.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 65.50:
                                            return 8.0
                                        if sum_spades_values > 65.50:
                                            if num_spades <= 9.50:
                                                if num_nt_kings <= 1.00:
                                                    return 8.0
                                                if num_nt_kings > 1.00:
                                                    if num_nt_kings <= 2.50:
                                                        return 9.0
                                                    if num_nt_kings > 2.50:
                                                        return 11.0
                                            if num_spades > 9.50:
                                                return 8.0
                                    if num_void_suits > 0.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 64.00:
                                                return 9.0
                                            if sum_spades_values > 64.00:
                                                if num_spades <= 9.50:
                                                    return 8.0
                                                if num_spades > 9.50:
                                                    return 9.0
                                        if num_nt_kings > 0.50:
                                            if num_void_suits <= 1.50:
                                                if num_nt_kings <= 1.50:
                                                    if sum_spades_values <= 63.00:
                                                        return 8.0
                                                    if sum_spades_values > 63.00:
                                                        return 9.0
                                                if num_nt_kings > 1.50:
                                                    if sum_spades_values <= 65.50:
                                                        return 9.0
                                                    if sum_spades_values > 65.50:
                                                        return 10.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 63.50:
                                                    return 10.0
                                                if sum_spades_values > 63.50:
                                                    return 9.0
                            if sum_spades_values > 66.50:
                                if num_nt_kings <= 0.50:
                                    if sum_spades_values <= 68.50:
                                        if sum_spades_values <= 67.50:
                                            if num_void_suits <= 1.50:
                                                if num_spades <= 9.50:
                                                    return 8.0
                                                if num_spades > 9.50:
                                                    return 9.0
                                            if num_void_suits > 1.50:
                                                return 9.0
                                        if sum_spades_values > 67.50:
                                            if num_void_suits <= 0.50:
                                                if num_spades <= 9.50:
                                                    return 8.0
                                                if num_spades > 9.50:
                                                    return 9.0
                                            if num_void_suits > 0.50:
                                                return 9.0
                                    if sum_spades_values > 68.50:
                                        return 9.0
                                if num_nt_kings > 0.50:
                                    if num_spades <= 9.50:
                                        if sum_spades_values <= 68.50:
                                            if num_void_suits <= 0.50:
                                                return 9.0
                                            if num_void_suits > 0.50:
                                                if num_nt_kings <= 1.50:
                                                    return 9.0
                                                if num_nt_kings > 1.50:
                                                    return 10.0
                                        if sum_spades_values > 68.50:
                                            if num_void_suits <= 1.50:
                                                return 9.0
                                            if num_void_suits > 1.50:
                                                return 11.0
                                    if num_spades > 9.50:
                                        return 9.0
                        if num_nt_aces > 0.50:
                            if num_nt_kings <= 0.50:
                                if sum_spades_values <= 68.50:
                                    if num_spades <= 9.50:
                                        if sum_spades_values <= 63.50:
                                            return 9.0
                                        if sum_spades_values > 63.50:
                                            if sum_spades_values <= 67.50:
                                                if num_void_suits <= 1.50:
                                                    return 9.0
                                                if num_void_suits > 1.50:
                                                    return 10.0
                                            if sum_spades_values > 67.50:
                                                return 9.0
                                    if num_spades > 9.50:
                                        return 9.0
                                if sum_spades_values > 68.50:
                                    if num_spades <= 9.50:
                                        if num_void_suits <= 0.50:
                                            return 9.0
                                        if num_void_suits > 0.50:
                                            return 10.0
                                    if num_spades > 9.50:
                                        return 10.0
                            if num_nt_kings > 0.50:
                                if sum_spades_values <= 65.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_kings <= 2.50:
                                            if num_nt_kings <= 1.50:
                                                return 9.0
                                            if num_nt_kings > 1.50:
                                                if sum_spades_values <= 64.00:
                                                    return 9.0
                                                if sum_spades_values > 64.00:
                                                    return 10.0
                                        if num_nt_kings > 2.50:
                                            return 10.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 64.50:
                                            return 10.0
                                        if sum_spades_values > 64.50:
                                            return 11.0
                                if sum_spades_values > 65.50:
                                    if num_spades <= 9.50:
                                        if sum_spades_values <= 66.50:
                                            if num_nt_kings <= 2.00:
                                                if num_void_suits <= 1.50:
                                                    return 10.0
                                                if num_void_suits > 1.50:
                                                    return 12.0
                                            if num_nt_kings > 2.00:
                                                return 10.0
                                        if sum_spades_values > 66.50:
                                            if num_nt_kings <= 1.50:
                                                if num_void_suits <= 1.00:
                                                    return 10.0
                                                if num_void_suits > 1.00:
                                                    return 11.0
                                            if num_nt_kings > 1.50:
                                                return 10.0
                                    if num_spades > 9.50:
                                        return 10.0
                if num_nt_aces > 1.50:
                    if num_nt_kings <= 0.50:
                        if num_spades <= 7.50:
                            if sum_spades_values <= 65.50:
                                if num_spades <= 6.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_aces <= 2.50:
                                            return 8.0
                                        if num_nt_aces > 2.50:
                                            return 9.0
                                    if num_void_suits > 0.50:
                                        return 9.0
                                if num_spades > 6.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 63.50:
                                            return 9.0
                                        if sum_spades_values > 63.50:
                                            if sum_spades_values <= 64.50:
                                                return 10.0
                                            if sum_spades_values > 64.50:
                                                return 9.0
                                    if num_void_suits > 0.50:
                                        return 9.0
                            if sum_spades_values > 65.50:
                                if num_nt_aces <= 2.50:
                                    if num_void_suits <= 0.50:
                                        return 9.0
                                    if num_void_suits > 0.50:
                                        if num_spades <= 6.50:
                                            return 9.0
                                        if num_spades > 6.50:
                                            return 10.0
                                if num_nt_aces > 2.50:
                                    if num_spades <= 6.50:
                                        if sum_spades_values <= 67.00:
                                            return 9.0
                                        if sum_spades_values > 67.00:
                                            return 10.0
                                    if num_spades > 6.50:
                                        return 10.0
                        if num_spades > 7.50:
                            if num_spades <= 8.50:
                                if num_nt_aces <= 2.50:
                                    if sum_spades_values <= 65.50:
                                        if sum_spades_values <= 62.50:
                                            return 9.0
                                        if sum_spades_values > 62.50:
                                            if num_void_suits <= 0.50:
                                                return 9.0
                                            if num_void_suits > 0.50:
                                                return 10.0
                                    if sum_spades_values > 65.50:
                                        if num_void_suits <= 0.50:
                                            return 9.0
                                        if num_void_suits > 0.50:
                                            return 10.0
                                if num_nt_aces > 2.50:
                                    if sum_spades_values <= 68.50:
                                        return 10.0
                                    if sum_spades_values > 68.50:
                                        return 11.0
                            if num_spades > 8.50:
                                if sum_spades_values <= 61.50:
                                    if sum_spades_values <= 60.50:
                                        return 10.0
                                    if sum_spades_values > 60.50:
                                        return 9.0
                                if sum_spades_values > 61.50:
                                    if num_nt_aces <= 2.50:
                                        if num_spades <= 9.50:
                                            return 10.0
                                        if num_spades > 9.50:
                                            return 11.0
                                    if num_nt_aces > 2.50:
                                        if sum_spades_values <= 62.50:
                                            return 10.0
                                        if sum_spades_values > 62.50:
                                            return 11.0
                    if num_nt_kings > 0.50:
                        if num_nt_kings <= 1.50:
                            if num_spades <= 7.50:
                                if num_nt_aces <= 2.50:
                                    if num_void_suits <= 0.50:
                                        if sum_spades_values <= 68.50:
                                            return 9.0
                                        if sum_spades_values > 68.50:
                                            return 10.0
                                    if num_void_suits > 0.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 65.00:
                                                return 9.0
                                            if sum_spades_values > 65.00:
                                                return 10.0
                                        if num_spades > 6.50:
                                            return 10.0
                                if num_nt_aces > 2.50:
                                    if num_spades <= 6.50:
                                        return 10.0
                                    if num_spades > 6.50:
                                        if sum_spades_values <= 65.50:
                                            return 10.0
                                        if sum_spades_values > 65.50:
                                            if sum_spades_values <= 67.00:
                                                return 11.0
                                            if sum_spades_values > 67.00:
                                                if sum_spades_values <= 68.50:
                                                    return 10.0
                                                if sum_spades_values > 68.50:
                                                    return 11.0
                            if num_spades > 7.50:
                                if sum_spades_values <= 65.50:
                                    if num_nt_aces <= 2.50:
                                        if num_void_suits <= 0.50:
                                            if sum_spades_values <= 63.50:
                                                if num_spades <= 8.50:
                                                    if sum_spades_values <= 61.50:
                                                        return 9.0
                                                    if sum_spades_values > 61.50:
                                                        return 10.0
                                                if num_spades > 8.50:
                                                    if sum_spades_values <= 60.50:
                                                        return 10.0
                                                    if sum_spades_values > 60.50:
                                                        if sum_spades_values <= 62.50:
                                                            return 11.0
                                                        if sum_spades_values > 62.50:
                                                            return 9.0
                                            if sum_spades_values > 63.50:
                                                if sum_spades_values <= 64.50:
                                                    return 10.0
                                                if sum_spades_values > 64.50:
                                                    if num_spades <= 8.50:
                                                        return 10.0
                                                    if num_spades > 8.50:
                                                        return 11.0
                                        if num_void_suits > 0.50:
                                            if num_spades <= 8.50:
                                                return 10.0
                                            if num_spades > 8.50:
                                                if sum_spades_values <= 62.50:
                                                    if sum_spades_values <= 60.50:
                                                        return 11.0
                                                    if sum_spades_values > 60.50:
                                                        return 10.0
                                                if sum_spades_values > 62.50:
                                                    return 11.0
                                    if num_nt_aces > 2.50:
                                        if num_spades <= 8.50:
                                            if sum_spades_values <= 62.50:
                                                return 10.0
                                            if sum_spades_values > 62.50:
                                                return 11.0
                                        if num_spades > 8.50:
                                            return 12.0
                                if sum_spades_values > 65.50:
                                    if num_spades <= 8.50:
                                        if num_void_suits <= 0.50:
                                            if num_nt_aces <= 2.50:
                                                return 10.0
                                            if num_nt_aces > 2.50:
                                                return 11.0
                                        if num_void_suits > 0.50:
                                            return 11.0
                                    if num_spades > 8.50:
                                        return 11.0
                        if num_nt_kings > 1.50:
                            if num_void_suits <= 0.50:
                                if num_nt_aces <= 2.50:
                                    if num_nt_kings <= 2.50:
                                        if num_spades <= 6.50:
                                            if sum_spades_values <= 66.00:
                                                return 9.0
                                            if sum_spades_values > 66.00:
                                                return 10.0
                                        if num_spades > 6.50:
                                            if num_spades <= 7.50:
                                                if sum_spades_values <= 61.00:
                                                    return 9.0
                                                if sum_spades_values > 61.00:
                                                    return 10.0
                                            if num_spades > 7.50:
                                                if sum_spades_values <= 66.50:
                                                    if sum_spades_values <= 64.50:
                                                        return 10.0
                                                    if sum_spades_values > 64.50:
                                                        return 11.0
                                                if sum_spades_values > 66.50:
                                                    return 10.0
                                    if num_nt_kings > 2.50:
                                        if sum_spades_values <= 65.50:
                                            return 10.0
                                        if sum_spades_values > 65.50:
                                            if sum_spades_values <= 68.50:
                                                if sum_spades_values <= 66.50:
                                                    return 11.0
                                                if sum_spades_values > 66.50:
                                                    if sum_spades_values <= 67.50:
                                                        return 10.0
                                                    if sum_spades_values > 67.50:
                                                        return 11.0
                                            if sum_spades_values > 68.50:
                                                return 9.0
                                if num_nt_aces > 2.50:
                                    if sum_spades_values <= 61.50:
                                        return 11.0
                                    if sum_spades_values > 61.50:
                                        if sum_spades_values <= 64.00:
                                            return 10.0
                                        if sum_spades_values > 64.00:
                                            if sum_spades_values <= 66.50:
                                                return 11.0
                                            if sum_spades_values > 66.50:
                                                if sum_spades_values <= 67.50:
                                                    return 12.0
                                                if sum_spades_values > 67.50:
                                                    if num_spades <= 6.50:
                                                        return 11.0
                                                    if num_spades > 6.50:
                                                        return 10.0
                            if num_void_suits > 0.50:
                                if num_spades <= 6.50:
                                    if sum_spades_values <= 66.00:
                                        return 10.0
                                    if sum_spades_values > 66.00:
                                        if sum_spades_values <= 67.50:
                                            return 11.0
                                        if sum_spades_values > 67.50:
                                            return 10.0
                                if num_spades > 6.50:
                                    if sum_spades_values <= 68.50:
                                        if sum_spades_values <= 63.50:
                                            if num_spades <= 7.50:
                                                return 10.0
                                            if num_spades > 7.50:
                                                return 11.0
                                        if sum_spades_values > 63.50:
                                            return 11.0
                                    if sum_spades_values > 68.50:
                                        return 10.0
            if sum_spades_values > 69.50:
                if sum_spades_values <= 79.50:
                    if num_spades <= 7.50:
                        if num_nt_kings <= 1.50:
                            if num_nt_kings <= 0.50:
                                if num_nt_aces <= 0.50:
                                    if num_void_suits <= 0.50:
                                        return 7.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 75.00:
                                            if num_void_suits <= 1.50:
                                                return 8.0
                                            if num_void_suits > 1.50:
                                                if sum_spades_values <= 72.50:
                                                    if sum_spades_values <= 71.00:
                                                        return 9.0
                                                    if sum_spades_values > 71.00:
                                                        return 10.0
                                                if sum_spades_values > 72.50:
                                                    return 9.0
                                        if sum_spades_values > 75.00:
                                            return 8.0
                                if num_nt_aces > 0.50:
                                    if sum_spades_values <= 72.50:
                                        if sum_spades_values <= 71.00:
                                            if num_void_suits <= 0.50:
                                                if num_nt_aces <= 1.50:
                                                    return 8.0
                                                if num_nt_aces > 1.50:
                                                    return 9.0
                                            if num_void_suits > 0.50:
                                                if num_nt_aces <= 1.50:
                                                    return 9.0
                                                if num_nt_aces > 1.50:
                                                    return 10.0
                                        if sum_spades_values > 71.00:
                                            if num_void_suits <= 0.50:
                                                return 8.0
                                            if num_void_suits > 0.50:
                                                if num_void_suits <= 1.50:
                                                    return 9.0
                                                if num_void_suits > 1.50:
                                                    return 10.0
                                    if sum_spades_values > 72.50:
                                        if num_nt_aces <= 1.50:
                                            if sum_spades_values <= 76.50:
                                                if num_void_suits <= 1.50:
                                                    return 9.0
                                                if num_void_suits > 1.50:
                                                    return 10.0
                                            if sum_spades_values > 76.50:
                                                return 9.0
                                        if num_nt_aces > 1.50:
                                            if sum_spades_values <= 74.00:
                                                if num_void_suits <= 0.50:
                                                    return 9.0
                                                if num_void_suits > 0.50:
                                                    return 10.0
                                            if sum_spades_values > 74.00:
                                                return 10.0
                            if num_nt_kings > 0.50:
                                if num_nt_aces <= 1.50:
                                    if num_nt_aces <= 0.50:
                                        if num_void_suits <= 0.50:
                                            return 8.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 70.50:
                                                if num_void_suits <= 1.50:
                                                    return 8.0
                                                if num_void_suits > 1.50:
                                                    return 10.0
                                            if sum_spades_values > 70.50:
                                                if num_void_suits <= 1.50:
                                                    return 9.0
                                                if num_void_suits > 1.50:
                                                    if sum_spades_values <= 72.00:
                                                        return 9.0
                                                    if sum_spades_values > 72.00:
                                                        return 10.0
                                    if num_nt_aces > 0.50:
                                        if num_void_suits <= 0.50:
                                            return 9.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 71.50:
                                                return 10.0
                                            if sum_spades_values > 71.50:
                                                if num_void_suits <= 1.50:
                                                    return 10.0
                                                if num_void_suits > 1.50:
                                                    if sum_spades_values <= 74.00:
                                                        return 9.0
                                                    if sum_spades_values > 74.00:
                                                        return 10.0
                                if num_nt_aces > 1.50:
                                    if num_void_suits <= 0.50:
                                        if num_nt_aces <= 2.50:
                                            return 10.0
                                        if num_nt_aces > 2.50:
                                            return 11.0
                                    if num_void_suits > 0.50:
                                        if sum_spades_values <= 75.50:
                                            if sum_spades_values <= 73.50:
                                                return 11.0
                                            if sum_spades_values > 73.50:
                                                return 10.0
                                        if sum_spades_values > 75.50:
                                            return 11.0
                        if num_nt_kings > 1.50:
                            if num_nt_aces <= 0.50:
                                if sum_spades_values <= 73.00:
                                    if num_void_suits <= 0.50:
                                        return 8.0
                                    if num_void_suits > 0.50:
                                        return 9.0
                                if sum_spades_values > 73.00:
                                    return 9.0
                            if num_nt_aces > 0.50:
                                if num_void_suits <= 0.50:
                                    if sum_spades_values <= 70.50:
                                        return 11.0
                                    if sum_spades_values > 70.50:
                                        if num_nt_aces <= 2.50:
                                            if num_nt_kings <= 2.50:
                                                if num_nt_aces <= 1.50:
                                                    if sum_spades_values <= 73.00:
                                                        return 9.0
                                                    if sum_spades_values > 73.00:
                                                        return 10.0
                                                if num_nt_aces > 1.50:
                                                    if sum_spades_values <= 73.00:
                                                        return 10.0
                                                    if sum_spades_values > 73.00:
                                                        if sum_spades_values <= 75.50:
                                                            return 11.0
                                                        if sum_spades_values > 75.50:
                                                            if sum_spades_values <= 76.50:
                                                                return 10.0
                                                            if sum_spades_values > 76.50:
                                                                return 11.0
                                            if num_nt_kings > 2.50:
                                                if num_nt_aces <= 1.50:
                                                    return 10.0
                                                if num_nt_aces > 1.50:
                                                    return 11.0
                                        if num_nt_aces > 2.50:
                                            return 9.0
                                if num_void_suits > 0.50:
                                    if sum_spades_values <= 71.50:
                                        if sum_spades_values <= 70.50:
                                            if num_nt_aces <= 1.50:
                                                return 10.0
                                            if num_nt_aces > 1.50:
                                                return 11.0
                                        if sum_spades_values > 70.50:
                                            return 10.0
                                    if sum_spades_values > 71.50:
                                        if num_nt_aces <= 1.50:
                                            if sum_spades_values <= 76.00:
                                                return 10.0
                                            if sum_spades_values > 76.00:
                                                return 11.0
                                        if num_nt_aces > 1.50:
                                            return 11.0
                    if num_spades > 7.50:
                        if num_nt_kings <= 2.50:
                            if num_void_suits <= 1.50:
                                if num_nt_aces <= 0.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 9.50:
                                            if sum_spades_values <= 72.50:
                                                if num_void_suits <= 0.50:
                                                    return 8.0
                                                if num_void_suits > 0.50:
                                                    return 9.0
                                            if sum_spades_values > 72.50:
                                                if num_spades <= 8.50:
                                                    if num_void_suits <= 0.50:
                                                        return 8.0
                                                    if num_void_suits > 0.50:
                                                        return 9.0
                                                if num_spades > 8.50:
                                                    return 9.0
                                        if num_spades > 9.50:
                                            if num_spades <= 10.50:
                                                if num_void_suits <= 0.50:
                                                    if sum_spades_values <= 75.50:
                                                        return 9.0
                                                    if sum_spades_values > 75.50:
                                                        return 10.0
                                                if num_void_suits > 0.50:
                                                    if sum_spades_values <= 75.00:
                                                        return 9.0
                                                    if sum_spades_values > 75.00:
                                                        return 10.0
                                            if num_spades > 10.50:
                                                return 10.0
                                    if num_nt_kings > 0.50:
                                        if sum_spades_values <= 75.50:
                                            if num_spades <= 9.50:
                                                if num_void_suits <= 0.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_spades <= 8.50:
                                                            if sum_spades_values <= 74.00:
                                                                return 8.0
                                                            if sum_spades_values > 74.00:
                                                                return 9.0
                                                        if num_spades > 8.50:
                                                            return 9.0
                                                    if num_nt_kings > 1.50:
                                                        return 9.0
                                                if num_void_suits > 0.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_spades <= 8.50:
                                                            return 9.0
                                                        if num_spades > 8.50:
                                                            if sum_spades_values <= 72.50:
                                                                return 9.0
                                                            if sum_spades_values > 72.50:
                                                                return 10.0
                                                    if num_nt_kings > 1.50:
                                                        return 10.0
                                            if num_spades > 9.50:
                                                if num_void_suits <= 0.50:
                                                    return 9.0
                                                if num_void_suits > 0.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 10.0
                                                    if num_nt_kings > 1.50:
                                                        if sum_spades_values <= 72.50:
                                                            return 10.0
                                                        if sum_spades_values > 72.50:
                                                            return 9.0
                                        if sum_spades_values > 75.50:
                                            if num_nt_kings <= 1.50:
                                                if num_void_suits <= 0.50:
                                                    if num_spades <= 9.50:
                                                        return 9.0
                                                    if num_spades > 9.50:
                                                        if sum_spades_values <= 76.50:
                                                            return 10.0
                                                        if sum_spades_values > 76.50:
                                                            if sum_spades_values <= 77.50:
                                                                return 9.0
                                                            if sum_spades_values > 77.50:
                                                                return 10.0
                                                if num_void_suits > 0.50:
                                                    return 10.0
                                            if num_nt_kings > 1.50:
                                                if sum_spades_values <= 78.50:
                                                    if num_void_suits <= 0.50:
                                                        if num_spades <= 8.50:
                                                            return 9.0
                                                        if num_spades > 8.50:
                                                            return 10.0
                                                    if num_void_suits > 0.50:
                                                        if num_spades <= 8.50:
                                                            return 10.0
                                                        if num_spades > 8.50:
                                                            if num_spades <= 9.50:
                                                                if sum_spades_values <= 77.50:
                                                                    return 10.0
                                                                if sum_spades_values > 77.50:
                                                                    return 11.0
                                                            if num_spades > 9.50:
                                                                if sum_spades_values <= 76.50:
                                                                    return 10.0
                                                                if sum_spades_values > 76.50:
                                                                    return 9.0
                                                if sum_spades_values > 78.50:
                                                    if num_spades <= 9.50:
                                                        return 10.0
                                                    if num_spades > 9.50:
                                                        return 13.0
                                if num_nt_aces > 0.50:
                                    if num_nt_aces <= 1.50:
                                        if num_void_suits <= 0.50:
                                            if num_spades <= 8.50:
                                                if sum_spades_values <= 72.50:
                                                    if num_nt_kings <= 1.50:
                                                        return 9.0
                                                    if num_nt_kings > 1.50:
                                                        return 10.0
                                                if sum_spades_values > 72.50:
                                                    if sum_spades_values <= 76.50:
                                                        if sum_spades_values <= 74.50:
                                                            return 10.0
                                                        if sum_spades_values > 74.50:
                                                            if sum_spades_values <= 75.50:
                                                                if num_nt_kings <= 0.50:
                                                                    return 9.0
                                                                if num_nt_kings > 0.50:
                                                                    return 10.0
                                                            if sum_spades_values > 75.50:
                                                                return 10.0
                                                    if sum_spades_values > 76.50:
                                                        if num_nt_kings <= 0.50:
                                                            return 9.0
                                                        if num_nt_kings > 0.50:
                                                            return 10.0
                                            if num_spades > 8.50:
                                                if sum_spades_values <= 71.00:
                                                    return 9.0
                                                if sum_spades_values > 71.00:
                                                    if sum_spades_values <= 76.50:
                                                        if num_nt_kings <= 1.50:
                                                            if num_spades <= 9.50:
                                                                if sum_spades_values <= 72.50:
                                                                    if num_nt_kings <= 0.50:
                                                                        return 9.0
                                                                    if num_nt_kings > 0.50:
                                                                        return 10.0
                                                                if sum_spades_values > 72.50:
                                                                    return 10.0
                                                            if num_spades > 9.50:
                                                                if num_nt_kings <= 0.50:
                                                                    if sum_spades_values <= 75.50:
                                                                        return 10.0
                                                                    if sum_spades_values > 75.50:
                                                                        return 9.0
                                                                if num_nt_kings > 0.50:
                                                                    if sum_spades_values <= 75.50:
                                                                        if sum_spades_values <= 74.00:
                                                                            return 10.0
                                                                        if sum_spades_values > 74.00:
                                                                            return 11.0
                                                                    if sum_spades_values > 75.50:
                                                                        return 10.0
                                                        if num_nt_kings > 1.50:
                                                            if sum_spades_values <= 73.50:
                                                                return 11.0
                                                            if sum_spades_values > 73.50:
                                                                if sum_spades_values <= 74.50:
                                                                    return 10.0
                                                                if sum_spades_values > 74.50:
                                                                    return 11.0
                                                    if sum_spades_values > 76.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 10.0
                                                        if num_nt_kings > 1.50:
                                                            if sum_spades_values <= 78.50:
                                                                return 11.0
                                                            if sum_spades_values > 78.50:
                                                                return 10.0
                                        if num_void_suits > 0.50:
                                            if sum_spades_values <= 75.50:
                                                if num_nt_kings <= 0.50:
                                                    if sum_spades_values <= 70.50:
                                                        if num_spades <= 8.50:
                                                            return 9.0
                                                        if num_spades > 8.50:
                                                            return 10.0
                                                    if sum_spades_values > 70.50:
                                                        return 10.0
                                                if num_nt_kings > 0.50:
                                                    if num_spades <= 8.50:
                                                        if num_nt_kings <= 1.50:
                                                            return 10.0
                                                        if num_nt_kings > 1.50:
                                                            if sum_spades_values <= 72.00:
                                                                return 10.0
                                                            if sum_spades_values > 72.00:
                                                                return 11.0
                                                    if num_spades > 8.50:
                                                        if sum_spades_values <= 74.50:
                                                            if sum_spades_values <= 71.50:
                                                                if num_spades <= 9.50:
                                                                    if num_nt_kings <= 1.50:
                                                                        return 10.0
                                                                    if num_nt_kings > 1.50:
                                                                        return 11.0
                                                                if num_spades > 9.50:
                                                                    return 11.0
                                                            if sum_spades_values > 71.50:
                                                                if num_nt_kings <= 1.50:
                                                                    if num_spades <= 9.50:
                                                                        return 11.0
                                                                    if num_spades > 9.50:
                                                                        if sum_spades_values <= 73.50:
                                                                            if sum_spades_values <= 72.50:
                                                                                return 10.0
                                                                            if sum_spades_values > 72.50:
                                                                                return 11.0
                                                                        if sum_spades_values > 73.50:
                                                                            return 10.0
                                                                if num_nt_kings > 1.50:
                                                                    return 11.0
                                                        if sum_spades_values > 74.50:
                                                            return 10.0
                                            if sum_spades_values > 75.50:
                                                if num_nt_kings <= 0.50:
                                                    if sum_spades_values <= 77.50:
                                                        if sum_spades_values <= 76.50:
                                                            return 10.0
                                                        if sum_spades_values > 76.50:
                                                            return 11.0
                                                    if sum_spades_values > 77.50:
                                                        return 10.0
                                                if num_nt_kings > 0.50:
                                                    if num_nt_kings <= 1.50:
                                                        if sum_spades_values <= 76.50:
                                                            return 11.0
                                                        if sum_spades_values > 76.50:
                                                            if sum_spades_values <= 78.00:
                                                                if num_spades <= 9.50:
                                                                    return 11.0
                                                                if num_spades > 9.50:
                                                                    return 12.0
                                                            if sum_spades_values > 78.00:
                                                                return 12.0
                                                    if num_nt_kings > 1.50:
                                                        if sum_spades_values <= 78.50:
                                                            return 11.0
                                                        if sum_spades_values > 78.50:
                                                            return 10.0
                                    if num_nt_aces > 1.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 75.50:
                                                if sum_spades_values <= 70.50:
                                                    if num_spades <= 8.50:
                                                        return 11.0
                                                    if num_spades > 8.50:
                                                        if num_nt_aces <= 2.50:
                                                            return 10.0
                                                        if num_nt_aces > 2.50:
                                                            return 11.0
                                                if sum_spades_values > 70.50:
                                                    if num_nt_aces <= 2.50:
                                                        if num_spades <= 8.50:
                                                            if num_void_suits <= 0.50:
                                                                return 10.0
                                                            if num_void_suits > 0.50:
                                                                if sum_spades_values <= 73.00:
                                                                    return 10.0
                                                                if sum_spades_values > 73.00:
                                                                    return 11.0
                                                        if num_spades > 8.50:
                                                            if num_void_suits <= 0.50:
                                                                if sum_spades_values <= 72.50:
                                                                    return 10.0
                                                                if sum_spades_values > 72.50:
                                                                    if sum_spades_values <= 74.50:
                                                                        return 11.0
                                                                    if sum_spades_values > 74.50:
                                                                        return 10.0
                                                            if num_void_suits > 0.50:
                                                                return 11.0
                                                    if num_nt_aces > 2.50:
                                                        if num_spades <= 8.50:
                                                            return 11.0
                                                        if num_spades > 8.50:
                                                            return 10.0
                                            if sum_spades_values > 75.50:
                                                if num_spades <= 8.50:
                                                    if num_void_suits <= 0.50:
                                                        if sum_spades_values <= 77.50:
                                                            if num_nt_aces <= 2.50:
                                                                return 10.0
                                                            if num_nt_aces > 2.50:
                                                                return 11.0
                                                        if sum_spades_values > 77.50:
                                                            return 10.0
                                                    if num_void_suits > 0.50:
                                                        return 11.0
                                                if num_spades > 8.50:
                                                    if num_void_suits <= 0.50:
                                                        if num_spades <= 9.50:
                                                            return 11.0
                                                        if num_spades > 9.50:
                                                            if num_nt_aces <= 2.50:
                                                                return 11.0
                                                            if num_nt_aces > 2.50:
                                                                return 12.0
                                                    if num_void_suits > 0.50:
                                                        if sum_spades_values <= 78.50:
                                                            if num_spades <= 9.50:
                                                                if sum_spades_values <= 77.50:
                                                                    return 11.0
                                                                if sum_spades_values > 77.50:
                                                                    return 12.0
                                                            if num_spades > 9.50:
                                                                return 12.0
                                                        if sum_spades_values > 78.50:
                                                            if num_spades <= 9.50:
                                                                return 11.0
                                                            if num_spades > 9.50:
                                                                return 12.0
                                        if num_nt_kings > 0.50:
                                            if num_nt_aces <= 2.50:
                                                if sum_spades_values <= 76.50:
                                                    if num_spades <= 8.50:
                                                        if sum_spades_values <= 72.00:
                                                            if num_void_suits <= 0.50:
                                                                return 10.0
                                                            if num_void_suits > 0.50:
                                                                return 11.0
                                                        if sum_spades_values > 72.00:
                                                            if sum_spades_values <= 74.50:
                                                                if num_void_suits <= 0.50:
                                                                    return 11.0
                                                                if num_void_suits > 0.50:
                                                                    if num_nt_kings <= 1.50:
                                                                        return 11.0
                                                                    if num_nt_kings > 1.50:
                                                                        return 12.0
                                                            if sum_spades_values > 74.50:
                                                                return 11.0
                                                    if num_spades > 8.50:
                                                        return 11.0
                                                if sum_spades_values > 76.50:
                                                    if num_nt_kings <= 1.50:
                                                        if sum_spades_values <= 77.50:
                                                            return 12.0
                                                        if sum_spades_values > 77.50:
                                                            if num_void_suits <= 0.50:
                                                                if num_spades <= 8.50:
                                                                    return 11.0
                                                                if num_spades > 8.50:
                                                                    if sum_spades_values <= 78.50:
                                                                        return 11.0
                                                                    if sum_spades_values > 78.50:
                                                                        return 12.0
                                                            if num_void_suits > 0.50:
                                                                if sum_spades_values <= 78.50:
                                                                    return 12.0
                                                                if sum_spades_values > 78.50:
                                                                    return 11.0
                                                    if num_nt_kings > 1.50:
                                                        if num_void_suits <= 0.50:
                                                            if sum_spades_values <= 78.50:
                                                                return 11.0
                                                            if sum_spades_values > 78.50:
                                                                return 8.0
                                                        if num_void_suits > 0.50:
                                                            return 12.0
                                            if num_nt_aces > 2.50:
                                                if num_nt_kings <= 1.50:
                                                    if sum_spades_values <= 73.50:
                                                        return 11.0
                                                    if sum_spades_values > 73.50:
                                                        return 12.0
                                                if num_nt_kings > 1.50:
                                                    return 12.0
                            if num_void_suits > 1.50:
                                if num_nt_aces <= 0.50:
                                    if sum_spades_values <= 73.50:
                                        if sum_spades_values <= 71.50:
                                            return 10.0
                                        if sum_spades_values > 71.50:
                                            if num_spades <= 8.50:
                                                return 10.0
                                            if num_spades > 8.50:
                                                if sum_spades_values <= 72.50:
                                                    if num_spades <= 9.50:
                                                        if num_nt_kings <= 0.50:
                                                            return 10.0
                                                        if num_nt_kings > 0.50:
                                                            return 11.0
                                                    if num_spades > 9.50:
                                                        return 11.0
                                                if sum_spades_values > 72.50:
                                                    return 12.0
                                    if sum_spades_values > 73.50:
                                        if num_nt_kings <= 0.50:
                                            if num_spades <= 8.50:
                                                return 11.0
                                            if num_spades > 8.50:
                                                if num_spades <= 9.50:
                                                    return 10.0
                                                if num_spades > 9.50:
                                                    if num_spades <= 10.50:
                                                        if sum_spades_values <= 76.50:
                                                            return 11.0
                                                        if sum_spades_values > 76.50:
                                                            return 10.0
                                                    if num_spades > 10.50:
                                                        return 11.0
                                        if num_nt_kings > 0.50:
                                            if num_spades <= 9.50:
                                                if num_spades <= 8.50:
                                                    if sum_spades_values <= 75.50:
                                                        if sum_spades_values <= 74.50:
                                                            return 11.0
                                                        if sum_spades_values > 74.50:
                                                            return 10.0
                                                    if sum_spades_values > 75.50:
                                                        return 11.0
                                                if num_spades > 8.50:
                                                    if sum_spades_values <= 76.50:
                                                        return 11.0
                                                    if sum_spades_values > 76.50:
                                                        if sum_spades_values <= 78.00:
                                                            return 10.0
                                                        if sum_spades_values > 78.00:
                                                            return 11.0
                                            if num_spades > 9.50:
                                                if sum_spades_values <= 77.00:
                                                    return 11.0
                                                if sum_spades_values > 77.00:
                                                    return 10.0
                                if num_nt_aces > 0.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 9.50:
                                            if num_spades <= 8.50:
                                                if sum_spades_values <= 74.00:
                                                    return 11.0
                                                if sum_spades_values > 74.00:
                                                    if sum_spades_values <= 76.00:
                                                        return 12.0
                                                    if sum_spades_values > 76.00:
                                                        if sum_spades_values <= 78.50:
                                                            return 11.0
                                                        if sum_spades_values > 78.50:
                                                            return 12.0
                                            if num_spades > 8.50:
                                                if sum_spades_values <= 71.50:
                                                    return 10.0
                                                if sum_spades_values > 71.50:
                                                    if sum_spades_values <= 74.50:
                                                        return 11.0
                                                    if sum_spades_values > 74.50:
                                                        if sum_spades_values <= 75.50:
                                                            return 12.0
                                                        if sum_spades_values > 75.50:
                                                            if sum_spades_values <= 76.50:
                                                                return 11.0
                                                            if sum_spades_values > 76.50:
                                                                return 12.0
                                        if num_spades > 9.50:
                                            if sum_spades_values <= 75.00:
                                                return 10.0
                                            if sum_spades_values > 75.00:
                                                return 11.0
                                    if num_nt_kings > 0.50:
                                        if num_spades <= 8.50:
                                            return 11.0
                                        if num_spades > 8.50:
                                            if sum_spades_values <= 73.50:
                                                return 11.0
                                            if sum_spades_values > 73.50:
                                                if num_spades <= 9.50:
                                                    if sum_spades_values <= 77.00:
                                                        return 12.0
                                                    if sum_spades_values > 77.00:
                                                        return 13.0
                                                if num_spades > 9.50:
                                                    return 12.0
                        if num_nt_kings > 2.50:
                            if sum_spades_values <= 76.50:
                                if sum_spades_values <= 71.50:
                                    return 12.0
                                if sum_spades_values > 71.50:
                                    if num_nt_aces <= 0.50:
                                        if num_spades <= 8.50:
                                            if sum_spades_values <= 74.50:
                                                return 9.0
                                            if sum_spades_values > 74.50:
                                                return 10.0
                                        if num_spades > 8.50:
                                            return 10.0
                                    if num_nt_aces > 0.50:
                                        return 10.0
                            if sum_spades_values > 76.50:
                                if sum_spades_values <= 78.50:
                                    if sum_spades_values <= 77.50:
                                        return 9.0
                                    if sum_spades_values > 77.50:
                                        if num_nt_aces <= 1.00:
                                            return 9.0
                                        if num_nt_aces > 1.00:
                                            return 12.0
                                if sum_spades_values > 78.50:
                                    return 9.0
                if sum_spades_values > 79.50:
                    if num_void_suits <= 0.50:
                        if sum_spades_values <= 93.00:
                            if num_nt_aces <= 0.50:
                                if num_nt_kings <= 0.50:
                                    if sum_spades_values <= 80.50:
                                        return 10.0
                                    if sum_spades_values > 80.50:
                                        if sum_spades_values <= 83.50:
                                            if sum_spades_values <= 82.00:
                                                if num_spades <= 9.50:
                                                    return 9.0
                                                if num_spades > 9.50:
                                                    return 10.0
                                            if sum_spades_values > 82.00:
                                                if num_spades <= 8.50:
                                                    return 8.0
                                                if num_spades > 8.50:
                                                    if num_spades <= 9.50:
                                                        return 9.0
                                                    if num_spades > 9.50:
                                                        return 10.0
                                        if sum_spades_values > 83.50:
                                            if num_spades <= 9.50:
                                                return 9.0
                                            if num_spades > 9.50:
                                                return 10.0
                                if num_nt_kings > 0.50:
                                    if sum_spades_values <= 87.50:
                                        if num_spades <= 9.50:
                                            if num_nt_kings <= 2.50:
                                                return 9.0
                                            if num_nt_kings > 2.50:
                                                if num_spades <= 8.50:
                                                    if sum_spades_values <= 82.00:
                                                        return 10.0
                                                    if sum_spades_values > 82.00:
                                                        if sum_spades_values <= 83.50:
                                                            return 9.0
                                                        if sum_spades_values > 83.50:
                                                            return 8.0
                                                if num_spades > 8.50:
                                                    return 10.0
                                        if num_spades > 9.50:
                                            if num_nt_kings <= 1.50:
                                                return 10.0
                                            if num_nt_kings > 1.50:
                                                return 11.0
                                    if sum_spades_values > 87.50:
                                        if sum_spades_values <= 88.50:
                                            return 10.0
                                        if sum_spades_values > 88.50:
                                            return 11.0
                            if num_nt_aces > 0.50:
                                if sum_spades_values <= 87.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 9.50:
                                            if num_nt_aces <= 2.50:
                                                if num_spades <= 8.50:
                                                    if sum_spades_values <= 80.50:
                                                        if num_nt_aces <= 1.50:
                                                            return 9.0
                                                        if num_nt_aces > 1.50:
                                                            return 10.0
                                                    if sum_spades_values > 80.50:
                                                        if sum_spades_values <= 82.50:
                                                            return 9.0
                                                        if sum_spades_values > 82.50:
                                                            if sum_spades_values <= 83.50:
                                                                return 10.0
                                                            if sum_spades_values > 83.50:
                                                                return 9.0
                                                if num_spades > 8.50:
                                                    if num_nt_aces <= 1.50:
                                                        return 10.0
                                                    if num_nt_aces > 1.50:
                                                        return 11.0
                                            if num_nt_aces > 2.50:
                                                if num_spades <= 8.50:
                                                    return 11.0
                                                if num_spades > 8.50:
                                                    return 12.0
                                        if num_spades > 9.50:
                                            if num_nt_aces <= 1.50:
                                                return 11.0
                                            if num_nt_aces > 1.50:
                                                return 12.0
                                    if num_nt_kings > 0.50:
                                        if num_nt_aces <= 1.50:
                                            if num_spades <= 8.50:
                                                return 10.0
                                            if num_spades > 8.50:
                                                if sum_spades_values <= 80.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_spades <= 9.50:
                                                            return 10.0
                                                        if num_spades > 9.50:
                                                            return 12.0
                                                    if num_nt_kings > 1.50:
                                                        return 11.0
                                                if sum_spades_values > 80.50:
                                                    if num_nt_kings <= 1.50:
                                                        if num_spades <= 9.50:
                                                            if sum_spades_values <= 85.50:
                                                                if sum_spades_values <= 82.50:
                                                                    return 10.0
                                                                if sum_spades_values > 82.50:
                                                                    if sum_spades_values <= 84.00:
                                                                        return 11.0
                                                                    if sum_spades_values > 84.00:
                                                                        return 10.0
                                                            if sum_spades_values > 85.50:
                                                                return 11.0
                                                        if num_spades > 9.50:
                                                            return 11.0
                                                    if num_nt_kings > 1.50:
                                                        return 11.0
                                        if num_nt_aces > 1.50:
                                            if num_nt_kings <= 1.50:
                                                if sum_spades_values <= 84.50:
                                                    return 11.0
                                                if sum_spades_values > 84.50:
                                                    return 12.0
                                            if num_nt_kings > 1.50:
                                                return 11.0
                                if sum_spades_values > 87.50:
                                    if num_spades <= 9.50:
                                        if num_nt_kings <= 0.50:
                                            if num_nt_aces <= 1.50:
                                                return 10.0
                                            if num_nt_aces > 1.50:
                                                return 11.0
                                        if num_nt_kings > 0.50:
                                            return 11.0
                                    if num_spades > 9.50:
                                        return 11.0
                        if sum_spades_values > 93.00:
                            return 10.0
                    if num_void_suits > 0.50:
                        if num_void_suits <= 1.50:
                            if sum_spades_values <= 82.50:
                                if num_nt_aces <= 0.50:
                                    if num_nt_kings <= 1.50:
                                        if num_spades <= 10.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 80.50:
                                                    return 10.0
                                                if sum_spades_values > 80.50:
                                                    if num_spades <= 8.50:
                                                        return 9.0
                                                    if num_spades > 8.50:
                                                        return 10.0
                                            if num_nt_kings > 0.50:
                                                return 10.0
                                        if num_spades > 10.50:
                                            return 11.0
                                    if num_nt_kings > 1.50:
                                        if sum_spades_values <= 81.50:
                                            if sum_spades_values <= 80.50:
                                                if num_spades <= 9.00:
                                                    return 10.0
                                                if num_spades > 9.00:
                                                    return 11.0
                                            if sum_spades_values > 80.50:
                                                if num_spades <= 9.50:
                                                    return 10.0
                                                if num_spades > 9.50:
                                                    return 11.0
                                        if sum_spades_values > 81.50:
                                            if num_spades <= 9.00:
                                                return 10.0
                                            if num_spades > 9.00:
                                                return 11.0
                                if num_nt_aces > 0.50:
                                    if num_nt_aces <= 1.50:
                                        if num_spades <= 8.50:
                                            if sum_spades_values <= 80.50:
                                                if num_nt_kings <= 0.50:
                                                    return 10.0
                                                if num_nt_kings > 0.50:
                                                    return 11.0
                                            if sum_spades_values > 80.50:
                                                if sum_spades_values <= 81.50:
                                                    return 10.0
                                                if sum_spades_values > 81.50:
                                                    if num_nt_kings <= 1.00:
                                                        return 10.0
                                                    if num_nt_kings > 1.00:
                                                        return 11.0
                                        if num_spades > 8.50:
                                            return 11.0
                                    if num_nt_aces > 1.50:
                                        if sum_spades_values <= 81.50:
                                            if sum_spades_values <= 80.50:
                                                if num_spades <= 8.50:
                                                    return 11.0
                                                if num_spades > 8.50:
                                                    if num_nt_kings <= 0.50:
                                                        if num_spades <= 9.50:
                                                            return 11.0
                                                        if num_spades > 9.50:
                                                            return 12.0
                                                    if num_nt_kings > 0.50:
                                                        return 12.0
                                            if sum_spades_values > 80.50:
                                                return 11.0
                                        if sum_spades_values > 81.50:
                                            if num_nt_kings <= 0.50:
                                                return 11.0
                                            if num_nt_kings > 0.50:
                                                if num_spades <= 8.50:
                                                    return 12.0
                                                if num_spades > 8.50:
                                                    return 13.0
                            if sum_spades_values > 82.50:
                                if num_nt_aces <= 0.50:
                                    if num_nt_kings <= 1.50:
                                        if num_nt_kings <= 0.50:
                                            if sum_spades_values <= 89.50:
                                                if sum_spades_values <= 87.50:
                                                    if sum_spades_values <= 85.50:
                                                        if num_spades <= 8.50:
                                                            return 9.0
                                                        if num_spades > 8.50:
                                                            if num_spades <= 10.50:
                                                                return 10.0
                                                            if num_spades > 10.50:
                                                                return 11.0
                                                    if sum_spades_values > 85.50:
                                                        if sum_spades_values <= 86.50:
                                                            if num_spades <= 10.50:
                                                                return 10.0
                                                            if num_spades > 10.50:
                                                                return 11.0
                                                        if sum_spades_values > 86.50:
                                                            if num_spades <= 10.50:
                                                                return 10.0
                                                            if num_spades > 10.50:
                                                                return 11.0
                                                if sum_spades_values > 87.50:
                                                    return 10.0
                                            if sum_spades_values > 89.50:
                                                if sum_spades_values <= 96.50:
                                                    if sum_spades_values <= 92.50:
                                                        if sum_spades_values <= 90.50:
                                                            if num_spades <= 10.00:
                                                                return 10.0
                                                            if num_spades > 10.00:
                                                                return 11.0
                                                        if sum_spades_values > 90.50:
                                                            return 11.0
                                                    if sum_spades_values > 92.50:
                                                        if num_spades <= 10.50:
                                                            if sum_spades_values <= 93.50:
                                                                return 11.0
                                                            if sum_spades_values > 93.50:
                                                                return 10.0
                                                        if num_spades > 10.50:
                                                            return 10.0
                                                if sum_spades_values > 96.50:
                                                    return 11.0
                                        if num_nt_kings > 0.50:
                                            if num_spades <= 9.50:
                                                return 10.0
                                            if num_spades > 9.50:
                                                if num_spades <= 10.50:
                                                    if sum_spades_values <= 83.50:
                                                        return 10.0
                                                    if sum_spades_values > 83.50:
                                                        return 11.0
                                                if num_spades > 10.50:
                                                    return 10.0
                                    if num_nt_kings > 1.50:
                                        return 11.0
                                if num_nt_aces > 0.50:
                                    if num_spades <= 8.50:
                                        if sum_spades_values <= 83.50:
                                            if num_nt_aces <= 1.50:
                                                if num_nt_kings <= 1.50:
                                                    return 10.0
                                                if num_nt_kings > 1.50:
                                                    return 12.0
                                            if num_nt_aces > 1.50:
                                                return 12.0
                                        if sum_spades_values > 83.50:
                                            if num_nt_kings <= 1.50:
                                                if num_nt_aces <= 1.50:
                                                    if num_nt_kings <= 0.50:
                                                        return 10.0
                                                    if num_nt_kings > 0.50:
                                                        return 11.0
                                                if num_nt_aces > 1.50:
                                                    return 12.0
                                            if num_nt_kings > 1.50:
                                                return 12.0
                                    if num_spades > 8.50:
                                        if num_nt_aces <= 1.50:
                                            if num_spades <= 10.50:
                                                if num_spades <= 9.50:
                                                    if sum_spades_values <= 86.50:
                                                        return 11.0
                                                    if sum_spades_values > 86.50:
                                                        if sum_spades_values <= 87.50:
                                                            return 12.0
                                                        if sum_spades_values > 87.50:
                                                            return 11.0
                                                if num_spades > 9.50:
                                                    if sum_spades_values <= 94.00:
                                                        if num_nt_kings <= 0.50:
                                                            return 11.0
                                                        if num_nt_kings > 0.50:
                                                            if sum_spades_values <= 86.50:
                                                                return 12.0
                                                            if sum_spades_values > 86.50:
                                                                if sum_spades_values <= 88.50:
                                                                    return 11.0
                                                                if sum_spades_values > 88.50:
                                                                    return 12.0
                                                    if sum_spades_values > 94.00:
                                                        return 13.0
                                            if num_spades > 10.50:
                                                return 12.0
                                        if num_nt_aces > 1.50:
                                            if num_nt_kings <= 0.50:
                                                if sum_spades_values <= 85.50:
                                                    return 11.0
                                                if sum_spades_values > 85.50:
                                                    if sum_spades_values <= 87.50:
                                                        return 12.0
                                                    if sum_spades_values > 87.50:
                                                        return 13.0
                                            if num_nt_kings > 0.50:
                                                return 13.0
                        if num_void_suits > 1.50:
                            if sum_spades_values <= 83.50:
                                if num_nt_aces <= 0.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 8.50:
                                            return 9.0
                                        if num_spades > 8.50:
                                            if sum_spades_values <= 80.50:
                                                return 10.0
                                            if sum_spades_values > 80.50:
                                                if num_spades <= 10.50:
                                                    return 11.0
                                                if num_spades > 10.50:
                                                    return 12.0
                                    if num_nt_kings > 0.50:
                                        if sum_spades_values <= 81.00:
                                            return 12.0
                                        if sum_spades_values > 81.00:
                                            return 9.0
                                if num_nt_aces > 0.50:
                                    if num_spades <= 9.50:
                                        if num_spades <= 8.50:
                                            return 11.0
                                        if num_spades > 8.50:
                                            if sum_spades_values <= 82.50:
                                                if sum_spades_values <= 81.00:
                                                    return 11.0
                                                if sum_spades_values > 81.00:
                                                    return 12.0
                                            if sum_spades_values > 82.50:
                                                return 11.0
                                    if num_spades > 9.50:
                                        if sum_spades_values <= 81.00:
                                            if num_nt_kings <= 0.50:
                                                return 11.0
                                            if num_nt_kings > 0.50:
                                                return 13.0
                                        if sum_spades_values > 81.00:
                                            if num_nt_kings <= 0.50:
                                                return 12.0
                                            if num_nt_kings > 0.50:
                                                return 13.0
                            if sum_spades_values > 83.50:
                                if num_nt_aces <= 0.50:
                                    if num_spades <= 8.50:
                                        return 13.0
                                    if num_spades > 8.50:
                                        if sum_spades_values <= 90.00:
                                            if sum_spades_values <= 87.50:
                                                if num_nt_kings <= 0.50:
                                                    if num_spades <= 9.50:
                                                        if sum_spades_values <= 86.00:
                                                            return 12.0
                                                        if sum_spades_values > 86.00:
                                                            return 10.0
                                                    if num_spades > 9.50:
                                                        if num_spades <= 10.50:
                                                            if sum_spades_values <= 85.50:
                                                                return 10.0
                                                            if sum_spades_values > 85.50:
                                                                return 11.0
                                                        if num_spades > 10.50:
                                                            return 12.0
                                                if num_nt_kings > 0.50:
                                                    if sum_spades_values <= 84.50:
                                                        return 11.0
                                                    if sum_spades_values > 84.50:
                                                        if num_spades <= 9.50:
                                                            return 12.0
                                                        if num_spades > 9.50:
                                                            return 11.0
                                            if sum_spades_values > 87.50:
                                                if num_spades <= 10.50:
                                                    if sum_spades_values <= 88.50:
                                                        if num_spades <= 9.50:
                                                            return 12.0
                                                        if num_spades > 9.50:
                                                            return 11.0
                                                    if sum_spades_values > 88.50:
                                                        if num_nt_kings <= 0.50:
                                                            return 11.0
                                                        if num_nt_kings > 0.50:
                                                            return 10.0
                                                if num_spades > 10.50:
                                                    return 12.0
                                        if sum_spades_values > 90.00:
                                            if sum_spades_values <= 91.50:
                                                if num_spades <= 10.50:
                                                    return 13.0
                                                if num_spades > 10.50:
                                                    return 12.0
                                            if sum_spades_values > 91.50:
                                                if num_nt_kings <= 0.50:
                                                    if num_spades <= 10.50:
                                                        if sum_spades_values <= 94.50:
                                                            return 12.0
                                                        if sum_spades_values > 94.50:
                                                            return 10.0
                                                    if num_spades > 10.50:
                                                        return 11.0
                                                if num_nt_kings > 0.50:
                                                    if sum_spades_values <= 92.50:
                                                        return 11.0
                                                    if sum_spades_values > 92.50:
                                                        if sum_spades_values <= 96.00:
                                                            if num_spades <= 10.50:
                                                                return 10.0
                                                            if num_spades > 10.50:
                                                                return 13.0
                                                        if sum_spades_values > 96.00:
                                                            return 11.0
                                if num_nt_aces > 0.50:
                                    if num_nt_kings <= 0.50:
                                        if num_spades <= 9.50:
                                            if sum_spades_values <= 84.50:
                                                return 13.0
                                            if sum_spades_values > 84.50:
                                                if sum_spades_values <= 85.50:
                                                    return 11.0
                                                if sum_spades_values > 85.50:
                                                    if sum_spades_values <= 87.50:
                                                        return 12.0
                                                    if sum_spades_values > 87.50:
                                                        return 11.0
                                        if num_spades > 9.50:
                                            if sum_spades_values <= 89.00:
                                                if sum_spades_values <= 85.50:
                                                    if sum_spades_values <= 84.50:
                                                        return 12.0
                                                    if sum_spades_values > 84.50:
                                                        return 13.0
                                                if sum_spades_values > 85.50:
                                                    return 12.0
                                            if sum_spades_values > 89.00:
                                                return 13.0
                                    if num_nt_kings > 0.50:
                                        if sum_spades_values <= 84.50:
                                            if num_spades <= 8.50:
                                                return 11.0
                                            if num_spades > 8.50:
                                                return 10.0
                                        if sum_spades_values > 84.50:
                                            return 12.0

# bid = determine_bid_number(c)
# print(bid)
