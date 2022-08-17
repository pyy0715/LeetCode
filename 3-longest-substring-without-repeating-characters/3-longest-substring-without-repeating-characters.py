class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length, start = 0, 0
        
        for i, char in enumerate(s):
            if char in used and start<=used[char]:
                start = used[char]+1
            else:
                max_length = max(max_length, i-start+1)
                
            used[char] = i
        return max_length
                
        