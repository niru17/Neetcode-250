class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c=1
        l=1
        nums=sorted(nums)
        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i]==1:
                c+=1
            elif nums[i+1]== nums[i]:
                continue
            else:
                c=1
            l=max(l,c)
        return l
        