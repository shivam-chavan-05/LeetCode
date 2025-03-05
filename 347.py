# Top K Frequent Elements 

from collections import Counter 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, freq in count.items():
            heapq.heappush(heap, (-freq,key))
        result = []
        while k >= 1:
            key = heapq.heappop(heap)
            result.append(key[1])
            k -=1
        return result
