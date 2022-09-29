import heapq

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        heapq.heapify(s)
        
        g.sort()
        count = 0

        for i in g:
            if not s:
                break
            
            while s:
                q = heapq.heappop(s)
                if i<=q:
                    count+=1
                    break
        return count
            
            