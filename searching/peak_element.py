class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        
        if nums[n-1] > nums[n-2]:
            return n-1

        def is_peak(idx):
            left =  float("-inf") if idx == 0 else nums[idx-1]
            right = float("-inf") if idx == n-1 else nums[idx+1]
            return nums[idx] > left and nums[idx] > right

        
        lo, hi = 1, n-2

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if is_peak(mid):
                return mid
            elif nums[mid-1] < nums[mid]:
                lo = mid+1
            else:
                hi = mid -1
        
        return None