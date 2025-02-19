#KoKo Eating Bananas 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)

            return True if hours <= h else False 
            
        L = 1
        R = max(piles)

        while L < R:
            k = (L + R) // 2
            if works(k):
                R = k
            else:
                L = k + 1
            
        return R
