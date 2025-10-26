class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH=[]
        for stone in stones:
            heapq.heappush(maxH,-stone)
        while len(maxH)>=2:
            y=heapq.heappop(maxH)
            x=heapq.heappop(maxH)
            if x!=y:
                heapq.heappush(maxH,(y-x))
        maxH.append(0)
        return -maxH[0]
            



        