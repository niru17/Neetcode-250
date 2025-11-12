class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[]
        for i in stones:
            heapq.heappush(maxHeap,-i)
        while len(maxHeap)>=2:
            y=heapq.heappop(maxHeap)
            x=heapq.heappop(maxHeap)
            if x!=y:
                heapq.heappush(maxHeap,(y-x))
        maxHeap.append(0)
        return -maxHeap[0]