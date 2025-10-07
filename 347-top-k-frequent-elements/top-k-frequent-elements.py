class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN={}
        for i in range(len(nums)):
            countN[nums[i]]=1+countN.get(nums[i],0)
        sorted_count=sorted(countN.items(),key=lambda x: x[1],reverse=True)
        res=[item[0] for item in sorted_count[:k]]
        return res

        