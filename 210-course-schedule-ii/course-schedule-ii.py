class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for course,pre in prerequisites:
            graph[pre].append(course)
        visited=set()
        path=set()
        cycle=False
        result=[]

        def dfs(course):
            nonlocal cycle 
            if course in path:
                cycle=True
                return
            if course in visited:
                return
            path.add(course)
            for nei in graph[course]:
                dfs(nei)
            path.remove(course)
            visited.add(course)
            result.append(course)

        for c in range(numCourses):
            if c not in visited:
                dfs(c)
        if cycle:
            return []
        return result[::-1]
        