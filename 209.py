# Minimum Size Subarray Sum


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        curr_sum = 0
        min_length = float('inf')
        
        for r in range(n):
            curr_sum += nums[r]
            
            while curr_sum >= target:
                min_length = min(min_length, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        
        return min_length if min_length != float('inf') else 0
