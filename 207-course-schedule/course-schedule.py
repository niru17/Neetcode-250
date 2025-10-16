class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        
        for course,pre in prerequisites:
            graph[pre].append(course)
        visited,path=set(),set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            path.remove(course)
            visited.add(course)
            return True
    
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True