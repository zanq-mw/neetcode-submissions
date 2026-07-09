"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # adj = defaultdict(list)
        # while node:
        #     for neighbor in node.neigbors:
        #         adj[node.val].append(neighbor.val)
        #     node = node.
        visited = {}

        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            
            n = Node(node.val)
            visited[node.val] = n
            for neighbor in node.neighbors:
                n.neighbors.append(dfs(neighbor))
            return n
        if node:
            return dfs(node)
        return None