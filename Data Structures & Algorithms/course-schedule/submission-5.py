class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if [] == prereqs.get(course):
                return True
            visited.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            prereqs[course] = []

            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True