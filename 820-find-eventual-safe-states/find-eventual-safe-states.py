class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        edge=defaultdict(list)
        outdeg=[0]*len(graph)
        for u in range(len(graph)):
            for v in graph[u]:
                edge[v].append(u)
                outdeg[u]+=1
        q=deque([i for i in range(len(graph)) if outdeg[i]==0])
        res=[]
        safe=[False]*len(graph)
        while q:
            node=q.popleft()
            safe[node]=True
            for nei in edge[node]:
                outdeg[nei]-=1
                if outdeg[nei]==0:
                    q.append(nei)
        
        return [i for i in range(len(graph)) if safe[i]]

        
        