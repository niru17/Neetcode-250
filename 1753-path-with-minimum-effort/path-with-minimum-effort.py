class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n=len(heights),len(heights[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        pq=[(0,0,0)]
        visited=set()
        while pq:
            effort,r,c=heapq.heappop(pq)
            if (r,c)==(m-1,n-1):
                return effort
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    new_effort=max(effort,abs(heights[r][c]-heights[nr][nc]))
                    heapq.heappush(pq,(new_effort,nr,nc))

            
