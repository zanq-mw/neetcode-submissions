class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(i, parent):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j != parent:
                    if not dfs(j, i):
                        return False
            # visited.remove(i)
            # adj[i] = []
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n