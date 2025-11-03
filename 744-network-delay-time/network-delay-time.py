class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float("inf")]*(n+1)
        dist[k]=0
        pq=[(0,k)]

        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            for u,nei,w in times:
                if dist[u]+w<dist[nei]:
                    dist[nei]=dist[u]+w
                    heapq.heappush(pq,(dist[nei],nei))
        ans=max(dist[1:])
        return -1 if ans==inf else ans        