class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap=[]
        res=[]
        for i in arr:
            dist=abs(i-x)
            heapq.heappush(maxheap,(-dist,-i))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        res = [-num for (_, num) in maxheap]
        return sorted(res)
        