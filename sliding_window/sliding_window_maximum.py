import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k >= n:
            return [max(nums)]

        l = r = 0
        q = collections.deque([])
        output = []

        while r < n:

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # outside bounds
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
