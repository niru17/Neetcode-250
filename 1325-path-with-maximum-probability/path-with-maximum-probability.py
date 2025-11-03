class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        for i, edge in enumerate(edges):
            u,v=edge
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        dist=[0.0] * n
        dist[start_node]=1.0
        pq=[(-1.0,start_node)]
        while pq:
            curr_prob,node=heapq.heappop(pq)
            curr_prob=-curr_prob
            if node==end_node:
                return curr_prob
            if curr_prob<dist[node]:
                continue
            for nei, prob in graph[node]:
                new_prob=curr_prob*prob
                if new_prob>dist[nei]:
                    dist[nei]=new_prob
                    heapq.heappush(pq,(-dist[nei],nei))
        return 0.0
        