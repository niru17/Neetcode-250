class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        total=0
        pq=[(0,0)]
        while pq and len(visited)<n:
            w,u=heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            total+=w
            for v in range(n):
                if v not in visited:
                    dist=abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])
                    heapq.heappush(pq,(dist,v))
        return total



        