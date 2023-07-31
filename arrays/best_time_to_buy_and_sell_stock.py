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


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
