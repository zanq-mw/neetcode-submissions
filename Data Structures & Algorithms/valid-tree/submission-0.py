class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            children = adj[node]
            visited.add(node)
            for child in children:
                if child == parent:
                    continue
                if child in visited:
                    return False
                if not dfs(child, node):
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n
