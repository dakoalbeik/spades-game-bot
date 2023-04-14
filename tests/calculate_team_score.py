import unittest


def calculate_team_score(bids, bids_won):
    round_scores = [0] * 4

    for i in range(4):
        if bids[i] == 0:
            round_scores[i] = 100 if bids_won[i] == 0 else -100
        elif i > 1 or bids[(i + 2) % 4] == 0:
            team_target_bids = bids[i] + bids[(i + 2) % 4]
            team_trick_count = bids_won[i] + bids_won[(i + 2) % 4]
            if team_trick_count < team_target_bids:
                round_scores[i] = (team_target_bids * -10)
            else:
                round_scores[i] = (team_target_bids * 10) + team_trick_count - team_target_bids
    return [round_scores[0] + round_scores[2], round_scores[1] + round_scores[3]]


def is_bid_won_valid(bids_won):
    if sum(bids_won) != 13:
        raise ValueError("The sum of bids_won should be 13")


class TestCalculateTeamScore(unittest.TestCase):

    def test_no_bids_no_tricks(self):
        bids = [0, 0, 0, 0]
        bids_won = [13, 0, 0, 0]
        is_bid_won_valid(bids_won)
        expected = [-30, 200]
        result = calculate_team_score(bids, bids_won)
        self.assertEqual(result, expected)

    def test_one_player_bids_nil_no_tricks(self):
        bids = [0, 2, 5, 6]
        bids_won = [0, 3, 5, 5]
        is_bid_won_valid(bids_won)
        expected = [150, 80]
        result = calculate_team_score(bids, bids_won)
        self.assertEqual(result, expected)

    # def test_one_player_bids_nil_some_tricks(self):
    #     bids = [0, 2, 5, 6]
    #     bids_won = [1, 3, 5, 4]
    #     is_bid_won_valid(bids_won)
    #     expected = [40, -40, 60, -60]
    #     result = calculate_team_score(bids, bids_won)
    #     self.assertEqual(result, expected)
    #
    # def test_one_team_fails_to_make_bid(self):
    #     bids = [3, 2, 5, 3]
    #     bids_won = [2, 3, 4, 2]
    #     is_bid_won_valid(bids_won)
    #     expected = [-80, 80, -20, 20]
    #     result = calculate_team_score(bids, bids_won)
    #     self.assertEqual(result, expected)
    #
    # def test_both_teams_make_bid(self):
    #     bids = [3, 2, 5, 3]
    #     bids_won = [3, 3, 6, 3]
    #     is_bid_won_valid(bids_won)
    #     expected = [10, 10, 30, 30]
    #     result = calculate_team_score(bids, bids_won)
    #     self.assertEqual(result, expected)
    #
    # def test_one_team_wins_all_tricks(self):
    #     bids = [3, 2, 5, 3]
    #     bids_won = [4, 0, 9, 0]
    #     is_bid_won_valid(bids_won)
    #     expected = [100, -100, 0, 0]
    #     result = calculate_team_score(bids, bids_won)
    #     self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
