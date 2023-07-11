from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calculate_score(scores):
            ten_reach = -1
            score = 0
            n = len(scores)

            for i in range(len(scores)):
                if scores[i] == 10:
                    if ten_reach >= i:
                        score += scores[i] * 2
                    else:
                        score += scores[i]
                    ten_reach = min(i + 2, n - 1)
                elif ten_reach >= i:
                    score += scores[i] * 2
                else:
                    score += scores[i]
            return score

        player_1_score, player_1_marker = calculate_score(player1), 1
        player_2_score, player_2_marker = calculate_score(player2), 2

        if player_1_score == player_2_score:
            return 0

        _, winner = max([(player_1_score, player_1_marker), (player_2_score, player_2_marker)], key=lambda x: x[0])

        return winner
