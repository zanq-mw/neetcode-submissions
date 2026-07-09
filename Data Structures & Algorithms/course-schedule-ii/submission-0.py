class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = defaultdict(list)
        for course, pre in prerequisites:
            reqs[course].append(pre)

        visited = set()
        order = []

        def dfs(course):
            if course in visited:
                return False
            
            if course not in reqs:
                reqs[course] == []
                order.append(course)
                return True

            # if reqs[course] == []:
            #     order.append(course)
            #     return True

            if reqs[course] == []:
                return True

            visited.add(course)

            for pre in reqs[course]:
                outcome = dfs(pre)
                if not outcome:
                    return False
            
            visited.remove(course)
            reqs[course] = []
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
