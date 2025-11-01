class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        for node in range(len(graph)):
            if node not in color:
                color[node]=0
                q=deque([node])
                while q:
                    cur=q.popleft()
                    for nei in graph[cur]:
                        if nei not in color:
                            color[nei]=1-color[cur]
                            q.append(nei)
                        elif color[nei]==color[cur]:
                            return False
        return True