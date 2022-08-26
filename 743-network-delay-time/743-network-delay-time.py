import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
            
        que = [(0, k)]
        dist = defaultdict(int)
        
        while que:
            time, node = heapq.heappop(que)
            if node not in dist:
                dist[node]=time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(que, (alt, v))
                    
        if len(dist)==n:
            return max(dist.values())
        return -1
                    
            