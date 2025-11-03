class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[float("inf")]*n
        dist[src]=0
        for _ in range(k+1):
            temp = dist.copy()
            updated=False
            for u,v,w in flights:
                if dist[u]!=float("inf") and dist[u]+w<temp[v]:
                    temp[v]=dist[u]+w
                    updated=True
            dist=temp
            if not updated:
                break
        return -1 if dist[dst]==float("inf") else dist[dst]


        