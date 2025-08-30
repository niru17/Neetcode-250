class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        m=len(nums)
        for i in range(m-1):
            if nums[i]==nums[i+1]:
                return True
        return False