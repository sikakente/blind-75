class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(lo, hi):
            
            while lo <= hi:
                mid = (lo+hi)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    hi = mid -1
                else:
                    lo = mid + 1
                    
            return -1
        
        N = len(nums)
        found_index = binary_search(0, N-1)
        
        if found_index == -1:
            return [-1, -1]
        start = end = found_index
        while start >= 0:
            if nums[start] != target:
                break
            start -= 1
        
        while end < N:
            if nums[end] != target:
                break
            end += 1
        
        return [max(start+1, 0), min(end-1, N)]