class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        charset=set(nums)
        for n in charset:
            if n-1 not in charset:
                length=0
                while n+length in charset:
                    length+=1
                longest=max(length,longest)
        return longest
        