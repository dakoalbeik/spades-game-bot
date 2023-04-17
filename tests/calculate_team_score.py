import unittest

# order of these two matter
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.spades_env import SpadesEnv


def is_bid_won_valid(tricks_won):
    if sum(tricks_won) != 13:
        raise ValueError("The sum of tricks_won should be 13")


class TestCalculateTeamScore(unittest.TestCase):

    def test_all_nil_one_person_wins_all(self):
        env = SpadesEnv()
        env.bids = [0, 0, 0, 0]
        env.tricks_won = [13, 0, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([0, 200], [13, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_one_player_bids_nil_and_gets_it(self):
        env = SpadesEnv()
        env.bids = [0, 2, 5, 6]
        env.tricks_won = [0, 3, 5, 5]
        is_bid_won_valid(env.tricks_won)
        expected = ([150, 80], [0, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_one_player_bids_nil_and_not_get(self):
        env = SpadesEnv()
        env.bids = [0, 2, 5, 6]
        env.tricks_won = [1, 3, 5, 4]
        is_bid_won_valid(env.tricks_won)
        expected = ([-50, -80], [1, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_one_team_fails_to_make_bid(self):
        env = SpadesEnv()
        env.bids = [3, 2, 5, 3]
        env.tricks_won = [3, 3, 4, 3]
        is_bid_won_valid(env.tricks_won)
        expected = ([-80, 50], [0, 1])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_team_two_fails_to_make_bid(self):
        env = SpadesEnv()
        env.bids = [3, 2, 5, 3]
        env.tricks_won = [3, 3, 6, 1]
        is_bid_won_valid(env.tricks_won)
        expected = ([80, -50], [1, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_one_team_wins_all_tricks(self):
        env = SpadesEnv()
        env.bids = [3, 2, 5, 3]
        env.tricks_won = [4, 0, 9, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([80, -50], [5, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_both_teammates_bid_nil_both_failed(self):
        env = SpadesEnv()
        env.bids = [0, 2, 0, 3]
        env.tricks_won = [1, 2, 1, 9]
        is_bid_won_valid(env.tricks_won)
        expected = ([-200, 50], [2, 6])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_01(self):
        env = SpadesEnv()
        env.bids = [3, 2, 0, 4]
        env.tricks_won = [4, 1, 3, 5]
        is_bid_won_valid(env.tricks_won)
        expected = ([-70, 60], [4, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_02(self):
        env = SpadesEnv()
        env.bids = [0, 2, 3, 1]
        env.tricks_won = [8, 3, 1, 1]
        is_bid_won_valid(env.tricks_won)
        expected = ([-70, 30], [6, 1])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_03(self):
        env = SpadesEnv()
        env.bids = [2, 3, 2, 0]
        env.tricks_won = [4, 8, 1, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([40, 130], [1, 5])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_04(self):
        env = SpadesEnv()
        env.bids = [4, 3, 1, 3]
        env.tricks_won = [13, 0, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([50, -60], [8, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_05(self):
        env = SpadesEnv()
        env.bids = [2, 2, 0, 5]
        env.tricks_won = [9, 4, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([120, -70], [7, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_06(self):
        env = SpadesEnv()
        env.bids = [0, 3, 1, 4]
        env.tricks_won = [1, 6, 1, 5]
        is_bid_won_valid(env.tricks_won)
        expected = ([-90, 70], [1, 4])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_07(self):
        env = SpadesEnv()
        env.bids = [3, 0, 4, 3]
        env.tricks_won = [4, 9, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([-70, -70], [0, 6])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_08(self):
        env = SpadesEnv()
        env.bids = [0, 1, 4, 0]
        env.tricks_won = [3, 0, 6, 4]
        is_bid_won_valid(env.tricks_won)
        expected = ([-60, -90], [5, 3])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_09(self):
        env = SpadesEnv()
        env.bids = [1, 3, 5, 2]
        env.tricks_won = [2, 10, 1, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([-60, 50], [0, 5])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_10(self):
        env = SpadesEnv()
        env.bids = [1, 0, 0, 5]
        env.tricks_won = [2, 10, 0, 1]
        is_bid_won_valid(env.tricks_won)
        expected = ([110, -50], [1, 6])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_11(self):
        env = SpadesEnv()
        env.bids = [1, 3, 4, 4]
        env.tricks_won = [6, 4, 1, 2]
        is_bid_won_valid(env.tricks_won)
        expected = ([50, -70], [2, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_12(self):
        env = SpadesEnv()
        env.bids = [1, 2, 1, 5]
        env.tricks_won = [11, 0, 2, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([20, -70], [11, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_13(self):
        env = SpadesEnv()
        env.bids = [3, 1, 5, 0]
        env.tricks_won = [9, 4, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([80, 110], [1, 3])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_14(self):
        env = SpadesEnv()
        env.bids = [2, 2, 0, 0]
        env.tricks_won = [5, 6, 0, 2]
        is_bid_won_valid(env.tricks_won)
        expected = ([120, -80], [3, 6])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_15(self):
        env = SpadesEnv()
        env.bids = [4, 2, 5, 3]
        env.tricks_won = [6, 0, 1, 6]
        is_bid_won_valid(env.tricks_won)
        expected = ([-90, 50], [0, 1])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_16(self):
        env = SpadesEnv()
        env.bids = [0, 0, 3, 2]
        env.tricks_won = [5, 8, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([-70, -80], [2, 6])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_17(self):
        env = SpadesEnv()
        env.bids = [5, 3, 2, 4]
        env.tricks_won = [13, 0, 0, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([70, -70], [6, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_18(self):
        env = SpadesEnv()
        env.bids = [1, 3, 5, 2]
        env.tricks_won = [2, 2, 7, 2]
        is_bid_won_valid(env.tricks_won)
        expected = ([60, -50], [3, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_19(self):
        env = SpadesEnv()
        env.bids = [3, 2, 5, 1]
        env.tricks_won = [1, 6, 6, 0]
        is_bid_won_valid(env.tricks_won)
        expected = ([-80, 30], [0, 3])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)

    def test_random_case_20(self):
        env = SpadesEnv()
        env.bids = [5, 5, 4, 2]
        env.tricks_won = [9, 1, 2, 1]
        is_bid_won_valid(env.tricks_won)
        expected = ([90, -70], [2, 0])
        result = env.calculate_team_round_score()
        self.assertEqual(expected, result)


if __name__ == "main":
    unittest.main()
