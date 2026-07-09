class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                # if child in visited:
                #     return False
                if not dfs(child, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n