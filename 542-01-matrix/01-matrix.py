class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        start=[]
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    start.append((r,c))
                else:
                    mat[r][c]=float("inf")
        q=deque(start)
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dirs:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n:
                        if mat[r][c]+1<mat[nr][nc]:
                            mat[nr][nc]=mat[r][c]+1
                            q.append((nr,nc))
        return mat
        