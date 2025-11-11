class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        path,visited=set(),set()
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visited.add(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




