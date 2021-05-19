from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s).items() == Counter(t).items():
            return True
        else:
            return False