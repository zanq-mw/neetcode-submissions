class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        processed = set()
        order = []

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            adj[course] = []
            if course not in processed:
                order.append(course)
                processed.add(course)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order