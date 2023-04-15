import csv
import random


def generate_spades_data(num_rows):
    with open('spades_data.csv', mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header row
        header_row = ['Player 1 Bid', 'Player 2 Bid', 'Player 3 Bid', 'Player 4 Bid',
                      'Player 1 Tricks', 'Player 2 Tricks', 'Player 3 Tricks', 'Player 4 Tricks']
        writer.writerow(header_row)

        for i in range(num_rows):
            # Generate random bids
            player1_bid = random.randint(0, 5)
            player2_bid = random.randint(0, 5)
            player3_bid = random.randint(0, 5)
            player4_bid = random.randint(0, 5)

            # Generate random tricks won
            tricks_won_sum = 0
            while tricks_won_sum != 13:
                player1_tricks = random.randint(0, 13)
                player2_tricks = random.randint(0, 13 - player1_tricks)
                player3_tricks = random.randint(0, 13 - player1_tricks - player2_tricks)
                player4_tricks = 13 - player1_tricks - player2_tricks - player3_tricks
                tricks_won_sum = player1_tricks + player2_tricks + player3_tricks + player4_tricks

            # Write row to CSV file
            row = [player1_bid, player2_bid, player3_bid, player4_bid,
                   player1_tricks, player2_tricks, player3_tricks, player4_tricks]
            writer.writerow(row)


generate_spades_data(20)
