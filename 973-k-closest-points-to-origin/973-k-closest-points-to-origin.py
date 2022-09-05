import math

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
            result.append((i, int(dis)))
            
        result.sort(key=lambda x: x[-1])
        
        answer = []
        for i in result[:k]:
            answer.append(points[i[0]])
        return answer
        
        
        
        