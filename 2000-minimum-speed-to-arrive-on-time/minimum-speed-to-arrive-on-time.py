class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1> hour:
            return -1
        l,r=1,10**7
        res=-1
        
        while l<=r:
            m=(l+r)//2
            time=0
            for i in range(len(dist)-1):
                time+=math.ceil(dist[i]/m)
            time+=dist[-1]/m
            
            if time<=hour+1e-9:
                res=m
                r=m-1
            else:
                l=m+1
        return res

        