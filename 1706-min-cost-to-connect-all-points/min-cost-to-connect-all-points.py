class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        parent=[i for i in range(n)]
        rank=[0]*n

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
        
        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                w=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((w,i,j))
        edges.sort()
        cost=0
        for w,i,j in edges:
            if union(i,j):
                cost+=w
        return cost


        