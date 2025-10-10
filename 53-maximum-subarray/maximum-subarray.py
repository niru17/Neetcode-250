class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=nums[0]
        max_sum=nums[0]
        for n in nums[1:]:
            curSum=max(n,curSum+n)
            max_sum=max(max_sum,curSum)
        return max_sum
        