import collections
import heapq, sys

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        weight = [(sys.maxsize, K)] * n
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, 0)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, cnt = heapq.heappop(Q)
            if node == dst:
                return price
            
            if cnt<=K:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < weight[v][0] or cnt+1 <= weight[v][1]:
                        weight[v] = (alt, cnt+1)
                        heapq.heappush(Q, (alt, v, cnt+1))
        return -1
        