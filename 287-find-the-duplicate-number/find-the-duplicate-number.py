class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sset=set()
        for n in nums:
            if n not in sset:
                sset.add(n)
            else:
                return n
                
        