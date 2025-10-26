class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for point in points:
            y,x=point[1],point[0]
            dist=x**2+y**2
            heapq.heappush(heap,(-dist,(x,y)))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

