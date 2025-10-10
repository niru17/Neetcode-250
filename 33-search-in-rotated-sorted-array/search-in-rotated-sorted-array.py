class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p_index=nums.index(min(nums))
        num_s=nums[p_index:]+nums[:p_index]
        l,r=0,len(num_s)-1
        while l<=r:
            mid=(l+r)//2
            if num_s[mid]==target:
                return nums.index(num_s[mid])
            elif num_s[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1