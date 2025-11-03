from collections import deque
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[0]*(n+1)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False
            if rank[px]<rank[py]:
                parent[px]=parent[py]
            if rank[px]>rank[py]:
                parent[py]=parent[px]
            else:
                parent[py]=parent[px]
                rank[px]+=1
            return True

        for u,v in edges:
            if not union(u,v):
                return[u,v]
        

        