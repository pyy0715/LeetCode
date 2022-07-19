from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_string = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            sorted_string[key].append(s)
        
            
        return sorted_string.values()