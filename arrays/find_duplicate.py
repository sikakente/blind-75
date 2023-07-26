class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow = nums[0]

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast