class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH=[]
        for stone in stones:
            heapq.heappush(maxH,-stone)
        if len(maxH)==1:
            return -maxH[0]
        if len(maxH)==0:
            return 0
        while len(maxH)>=2:
            y=heapq.heappop(maxH)
            x=heapq.heappop(maxH)
            if x!=y:
                new=abs(y-x)
                heapq.heappush(maxH,-new)
        return -maxH[0] if maxH else 0
            



        