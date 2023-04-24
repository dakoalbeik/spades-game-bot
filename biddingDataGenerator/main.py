from spades_game import SpadesGame


# Example game with four Bots
bot_names = ["Bot 1", "Bot 2", "Bot 3", "Bot 4"]
game = SpadesGame(bot_names)

# Play the game for 100,000 rounds and output the results to a text file
game.play_game(100000)
