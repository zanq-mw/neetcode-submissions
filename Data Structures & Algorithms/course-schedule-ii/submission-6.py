class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = defaultdict(list)
        for course, pre in prerequisites:
            reqs[course].append(pre)
        output = []
        visited = set()
        processed = set()

        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for pre in reqs[course]:
                if not dfs(pre):
                    return False
            if course not in processed:
                output.append(course)
            processed.add(course)
            visited.remove(course)
            # reqs[course] = []
            return True
        



        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output