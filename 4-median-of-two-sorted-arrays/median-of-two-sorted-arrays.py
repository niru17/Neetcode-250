class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        n=len(res)
        l,r=0,n-1
        m=(l+r)//2
        if len(res)%2==0:
            value= (res[n//2]+res[n//2 -1])/2.0
            return value
        else:
            return res[n//2]
            

        