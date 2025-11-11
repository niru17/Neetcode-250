class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m,n=len(grid),len(grid[0])
        visit=set()
        maxArea=0
        def dfs(r,c):
            area=0
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]==0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            grid[r][c]=0
            area+=1
            area+=dfs(r+1,c)
            area+=dfs(r-1,c)
            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    area=dfs(r,c)
                    maxArea=max(area,maxArea)
        return maxArea