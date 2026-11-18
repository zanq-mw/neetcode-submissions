class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        visited = set()

        adj = defaultdict(set)
        for root, node in edges:
            adj[root].add(node)
            adj[node].add(root)

        def dfs(node, root):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour != root:
                    if not dfs(neighbour, node):
                        return False
            return True
        print(visited)
        return dfs(0, None) and len(visited) == n

