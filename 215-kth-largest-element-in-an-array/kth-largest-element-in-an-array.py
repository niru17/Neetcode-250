class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=heapq.heappop(heap)
        return res

        