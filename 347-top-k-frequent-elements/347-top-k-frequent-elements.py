from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = sorted(Counter(nums).items(), key=lambda x: x[-1], reverse=True)
        return list(map(lambda x: x[0], frequency[:k]))
        
        