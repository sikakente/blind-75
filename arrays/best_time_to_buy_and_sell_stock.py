from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price - min_price)

        return profit

