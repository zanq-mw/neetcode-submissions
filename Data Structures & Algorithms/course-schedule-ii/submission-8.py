class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        visited = set()
        done = set()
        for course, pre in prerequisites:
            prereqs[course].append(pre)

        out = []

        def dfs(course):
            if course in visited:
                return False
            if course in done:
                return True
            visited.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            done.add(course)
            out.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return out