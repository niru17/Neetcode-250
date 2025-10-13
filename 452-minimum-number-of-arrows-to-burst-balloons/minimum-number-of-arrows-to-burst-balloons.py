class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res=1
        points.sort(key=lambda x:x[1])
        x=points[0][1]
        for i in range(1,len(points)):
            if x>= points[i][0]:
                continue
            else:
                res+=1
                x=points[i][1]
        return res
        