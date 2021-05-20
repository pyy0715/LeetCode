from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        case = defaultdict(list)
        for i, word in enumerate(s):
            case[word].append(i)
        
        for key, val in case.items():
            if len(val)==1:
                return val[0]
        return -1
        