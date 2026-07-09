"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}

        def dfs(node):
            if node.val in clones:
                return clones[node.val]
            res = Node(node.val)
            clones[node.val] = res

            for neighbor in node.neighbors:
                res.neighbors.append(dfs(neighbor))
            return res
        
        return dfs(node)