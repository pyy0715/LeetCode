from collections import defaultdict, deque

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        depart_dict = defaultdict(list)
        for i in tickets:
            depart_dict[i[0]].append(i[1])
            depart_dict[i[0]].sort()
        
        start = deque(['JFK'])
        res = []
        
        
        while start:
            while depart_dict[start[-1]]:
                start.append(depart_dict[start[-1]].pop(0))
                
            res.append(start.pop())
            
        return res[::-1]