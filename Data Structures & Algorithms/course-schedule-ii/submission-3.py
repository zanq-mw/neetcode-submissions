class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        result = []
        visited = set()
        processed = set()

        def dfs(i):
            if i in visited:
                return False
            if i in processed:
                return True
            visited.add(i)
            processed.add(i)
            for req in prereqs[i]:
                if not dfs(req):
                    return False
            visited.remove(i)
            result.append(i)
            # prereqs[i] = []
            return True
        


        for i in range(numCourses):
            print(i)
            if not dfs(i):
                return []
        return result