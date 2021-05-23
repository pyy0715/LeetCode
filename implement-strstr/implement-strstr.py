class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        
        m = len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+m]==needle:
                    return i
        return -1
                           
        
        
        