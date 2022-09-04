class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if result and result[-1][1]>=i[0]:
                result[-1][1] = max(result[-1][1], i[1])
                
            else:
                result.append(i)
                
        return result