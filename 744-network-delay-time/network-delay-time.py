class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float("inf")]*(n+1)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist[k]=0
        pq=[(0,k)]

        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            for nei,w in graph[node]:
                if dist[node]+w<dist[nei]:
                    dist[nei]=dist[node]+w
                    heapq.heappush(pq,(dist[nei],nei))
        ans=max(dist[1:])
        return -1 if ans==inf else ans        