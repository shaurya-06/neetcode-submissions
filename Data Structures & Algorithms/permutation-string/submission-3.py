from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        start, end = 0, len(s1)
        s1_chars = Counter(s1)

        while start <= len(s2) - len(s1):
            if Counter(s2[start:end]) == s1_chars:
                return True
            start += 1
            end += 1
        
        return False
        