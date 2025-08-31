class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countN={}
        m=len(nums)/2
        for i in range(len(nums)):
            countN[nums[i]]=1+countN.get(nums[i],0)
        for c in countN:
            if countN[c]>m:
                return c