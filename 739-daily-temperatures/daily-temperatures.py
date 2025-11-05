class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for i,t in enumerate(temperatures):
            while stack and temperatures[i]> temperatures[stack[-1]]:
                prev=stack.pop()
                res[prev]=i-prev
            stack.append(i)
        return res
        