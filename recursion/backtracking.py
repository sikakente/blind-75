from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        # find everyones balance
        balances = defaultdict(int)

        for transaction in transactions:
            giver, receiver, amount = transaction[0], transaction[1], transaction[2]
            balances[giver] -= amount
            balances[receiver] += amount

        # filter by only those with debts ie non zero accounts
        debts = [balance for balance in balances.values() if balance]
        num_debts = len(debts)

        def dfs(idx):
            while idx < num_debts and debts[idx] == 0:
                idx += 1

            if idx == num_debts:
                return 0

            ans = float("inf")

            for i in range(idx, num_debts):
                # if the current debt can be decreased
                if debts[i] * debts[idx] < 0:
                    debts[i] += debts[idx]
                    ans = min(ans, 1 + dfs(idx+1))
                    debts[i] -= debts[idx]
            return ans

        return dfs(0)
