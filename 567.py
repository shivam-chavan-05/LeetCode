# Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        count1 = [0] * 26  # Frequency for s1
        count2 = [0] * 26  # Frequency for current window in s2
        
        # Build frequency counts for s1 and the first window of s2
        for i in range(n):
            count1[ord(s1[i]) - 97] += 1
            count2[ord(s2[i]) - 97] += 1
        
        # Check if the first window matches
        if count1 == count2:
            return True
        
        # Slide the window through s2
        for r in range(n, m):
            # Add new char to the window
            count2[ord(s2[r]) - 97] += 1
            # Remove the char that's left behind
            count2[ord(s2[l]) - 97] -= 1
            l += 1
            # Compare the updated frequency with s1's frequency
            if count1 == count2:
                return True
                
        return False
