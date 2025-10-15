class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN={}
        for i in range(len(nums)):
            countN[nums[i]]=1+countN.get(nums[i],0)

        heap=[]
        for num in countN.keys():
            heapq.heappush(heap,(countN[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res





        