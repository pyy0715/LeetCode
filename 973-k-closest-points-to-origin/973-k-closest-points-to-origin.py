import math
import heapq

class Solution(object):
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        for i, p in enumerate(points):
            dis = math.pow(abs(p[0]),2) + math.pow(abs(p[1]),2)
            result.append((int(dis), p))
            
        heapq.heapify(result)
        answer = []
        while k:
            k-=1
            answer.append(heapq.heappop(result)[-1])
            
        return answer
            
        
        
        