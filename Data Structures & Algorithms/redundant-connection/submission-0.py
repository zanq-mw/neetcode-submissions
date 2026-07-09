class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = []
        for i in range(1, n+1):
            parents.append(i)

        rank = [1] * n

        def find(node):
            if parents[node-1] == node:
                return node
            p = find(parents[node-1])
            return p

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return False
            if rank[p1-1] > rank[p2-1]:
                parents[p2-1] = p1
                rank[p1-1] += rank[p2-1]
            else:
                parents[p1-1] = p2
                rank[p2-1] += rank[p1-1]
            return True

        for a, b in edges:
            if not union(a,b):
                return [a, b]