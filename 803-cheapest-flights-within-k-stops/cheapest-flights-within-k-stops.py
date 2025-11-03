class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        dist=[[float("inf")]*(k+2) for _ in range(n)]
        dist[src][0]=0
        pq=[(0,src,0)]

        while pq:
            cost,node,stops=heapq.heappop(pq)
            if node==dst:
                return cost
            if stops==k+1:
                continue
            for nei, w in graph[node]:
                new_cost=cost+w
                if new_cost<dist[nei][stops+1]:
                    dist[nei][stops+1]=new_cost
                    heapq.heappush(pq,(new_cost,nei,stops+1))
        return -1

        


        