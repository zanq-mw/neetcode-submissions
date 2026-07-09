class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqs = defaultdict(list)
        for course, pre in prerequisites:
            reqs[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            
            for pre in reqs[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            reqs[course] = []
            return True

        for course, _ in prerequisites:
            if not dfs(course):
                return False
        
        return True
                