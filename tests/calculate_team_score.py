import unittest


def calculate_team_round_score(bids, tricks_won):
    round_scores = [0, 0]
    round_bags = [0, 0]
    nil = 0

    for i in range(4):
        # if player goes nil
        team_mate = (i + 2) % 4
        curr_score = i % 2
        if bids[i] == nil:
            if tricks_won[i] == 0:
                round_scores[curr_score] += 100
            else:
                round_scores[curr_score] -= 100
                round_bags[curr_score] += tricks_won[i]
        # if player bid, and the score for the team is getting set for the first time, or the teammate bid nil
        # (meaning the current score doesn't account for this current player's score)
        elif round_scores[curr_score] == 0 or bids[team_mate] == nil:
            team_target_bids = bids[i] + bids[team_mate]
            team_trick_count = tricks_won[i] + tricks_won[team_mate]
            if team_trick_count < team_target_bids:
                round_scores[curr_score] -= team_target_bids * 10
            else:
                round_scores[curr_score] += team_target_bids * 10
                if bids[team_mate] == 0:
                    round_bags[curr_score] += tricks_won[i] - bids[i]
                else:
                    round_bags[curr_score] += team_trick_count - team_target_bids

    return round_scores, round_bags


def is_bid_won_valid(tricks_won):
    if sum(tricks_won) != 13:
        raise ValueError("The sum of tricks_won should be 13")


class TestCalculateTeamScore(unittest.TestCase):

    def test_all_nil_one_person_wins_all(self):
        bids = [0, 0, 0, 0]
        tricks_won = [13, 0, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([0, 200], [13, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_one_player_bids_nil_and_gets_it(self):
        bids = [0, 2, 5, 6]
        tricks_won = [0, 3, 5, 5]
        is_bid_won_valid(tricks_won)
        expected = ([150, 80], [0, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_one_player_bids_nil_and_not_get(self):
        bids = [0, 2, 5, 6]
        tricks_won = [1, 3, 5, 4]
        is_bid_won_valid(tricks_won)
        expected = ([-50, -80], [1, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_one_team_fails_to_make_bid(self):
        bids = [3, 2, 5, 3]
        tricks_won = [3, 3, 4, 3]
        is_bid_won_valid(tricks_won)
        expected = ([-80, 50], [0, 1])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_team_two_fails_to_make_bid(self):
        bids = [3, 2, 5, 3]
        tricks_won = [3, 3, 6, 1]
        is_bid_won_valid(tricks_won)
        expected = ([80, -50], [1, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_one_team_wins_all_tricks(self):
        bids = [3, 2, 5, 3]
        tricks_won = [4, 0, 9, 0]
        is_bid_won_valid(tricks_won)
        expected = ([80, -50], [5, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_both_teammates_bid_nil_both_failed(self):
        bids = [0, 2, 0, 3]
        tricks_won = [1, 2, 1, 9]
        is_bid_won_valid(tricks_won)
        expected = ([-200, 50], [2, 6])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_01(self):
        bids = [3, 2, 0, 4]
        tricks_won = [4, 1, 3, 5]
        is_bid_won_valid(tricks_won)
        expected = ([-70, 60], [4, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_02(self):
        bids = [0, 2, 3, 1]
        tricks_won = [8, 3, 1, 1]
        is_bid_won_valid(tricks_won)
        expected = ([-70, 30], [6, 1])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_03(self):
        bids = [2, 3, 2, 0]
        tricks_won = [4, 8, 1, 0]
        is_bid_won_valid(tricks_won)
        expected = ([40, 130], [1, 5])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_04(self):
        bids = [4, 3, 1, 3]
        tricks_won = [13, 0, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([50, -60], [8, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_05(self):
        bids = [2, 2, 0, 5]
        tricks_won = [9, 4, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([120, -70], [7, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_06(self):
        bids = [0, 3, 1, 4]
        tricks_won = [1, 6, 1, 5]
        is_bid_won_valid(tricks_won)
        expected = ([-90, 70], [1, 4])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_07(self):
        bids = [3, 0, 4, 3]
        tricks_won = [4, 9, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([-70, -70], [0, 6])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_08(self):
        bids = [0, 1, 4, 0]
        tricks_won = [3, 0, 6, 4]
        is_bid_won_valid(tricks_won)
        expected = ([-60, -90], [5, 3])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_09(self):
        bids = [1, 3, 5, 2]
        tricks_won = [2, 10, 1, 0]
        is_bid_won_valid(tricks_won)
        expected = ([-60, 50], [0, 5])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_10(self):
        bids = [1, 0, 0, 5]
        tricks_won = [2, 10, 0, 1]
        is_bid_won_valid(tricks_won)
        expected = ([110, -50], [1, 6])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_11(self):
        bids = [1, 3, 4, 4]
        tricks_won = [6, 4, 1, 2]
        is_bid_won_valid(tricks_won)
        expected = ([50, -70], [2, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_12(self):
        bids = [1, 2, 1, 5]
        tricks_won = [11, 0, 2, 0]
        is_bid_won_valid(tricks_won)
        expected = ([20, -70], [11, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_13(self):
        bids = [3, 1, 5, 0]
        tricks_won = [9, 4, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([80, 110], [1, 3])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_14(self):
        bids = [2, 2, 0, 0]
        tricks_won = [5, 6, 0, 2]
        is_bid_won_valid(tricks_won)
        expected = ([120, -80], [3, 6])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_15(self):
        bids = [4, 2, 5, 3]
        tricks_won = [6, 0, 1, 6]
        is_bid_won_valid(tricks_won)
        expected = ([-90, 50], [0, 1])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_16(self):
        bids = [0, 0, 3, 2]
        tricks_won = [5, 8, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([-70, -80], [2, 6])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_17(self):
        bids = [5, 3, 2, 4]
        tricks_won = [13, 0, 0, 0]
        is_bid_won_valid(tricks_won)
        expected = ([70, -70], [6, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_18(self):
        bids = [1, 3, 5, 2]
        tricks_won = [2, 2, 7, 2]
        is_bid_won_valid(tricks_won)
        expected = ([60, -50], [3, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_19(self):
        bids = [3, 2, 5, 1]
        tricks_won = [1, 6, 6, 0]
        is_bid_won_valid(tricks_won)
        expected = ([-80, 30], [0, 3])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)

    def test_random_case_20(self):
        bids = [5, 5, 4, 2]
        tricks_won = [9, 1, 2, 1]
        is_bid_won_valid(tricks_won)
        expected = ([90, -70], [2, 0])
        result = calculate_team_round_score(bids, tricks_won)
        self.assertEqual(expected, result)


if __name__ == "main":
    unittest.main()
