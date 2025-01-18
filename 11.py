#Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #greghogg
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
