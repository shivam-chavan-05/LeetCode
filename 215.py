#Kth Largest Element in an Array

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        while k >= 1:
            largest = heapq.heappop(nums)
            k -= 1

        return -largest
