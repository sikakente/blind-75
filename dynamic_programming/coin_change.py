from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        cache = {}

        def change(i, amount_left):
            if (amount_left, i) in cache:
                return cache[(amount_left, i)]
            if amount_left == 0:
                return 0

            if i == n:
                return float("inf")

            # including
            including = float("inf")
            if coins[i] <= amount_left:
                including = 1 + change(i, amount_left - coins[i])

            # exclusing current coint
            excluding = change(i + 1, amount_left)
            cache[(amount_left, i)] = min(including, excluding)
            return cache[(amount_left, i)]

        ans = change(0, amount)
        return -1 if ans == float("inf") else ans


class Solution2:

    def coin_change(self, coins: List[int], amount: int) -> int:
        denoms = coins
        n = amount
        all_change = [float("inf")] * (n + 1)
        all_change[0] = 0

        for target in range(1, n + 1):
            for denom in denoms:
                difference = target - denom
                if difference >= 0:
                    all_change[target] = min(all_change[difference] + 1, all_change[target])

        return all_change[n] if all_change[n] != float("inf") else -1