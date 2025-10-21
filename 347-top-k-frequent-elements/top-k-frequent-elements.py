class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        countN={}
        for num in nums:
            countN[num]=1+countN.get(num,0)
        
        for num in countN.keys():
            heapq.heappush(heap,(countN[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res


        