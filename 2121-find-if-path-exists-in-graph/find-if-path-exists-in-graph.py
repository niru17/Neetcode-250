class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if destination < 0 or destination >= n:
            return False
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist=[-1]*n
        dist[source]=0
        q=deque([source])
        while q:
            node=q.popleft()
            for nei in graph[node]:
                if dist[nei]==-1:
                    dist[nei]=dist[node]+1
                    q.append(nei)
        return dist[destination]!=-1
        

        