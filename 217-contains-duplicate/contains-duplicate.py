class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m=set()
        for i in nums:
            if i not in m:
                m.add(i)
            else:
                return True
        return False