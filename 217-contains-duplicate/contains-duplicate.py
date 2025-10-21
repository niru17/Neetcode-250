class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hassh=set()
        for i in nums:
            if i in hassh:
                return True
            else:
                hassh.add(i)
        return False
            
        