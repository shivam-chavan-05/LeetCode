#Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            M = (L + R) // 2

            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M

        min_index = R

        if min_index == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
