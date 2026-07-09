class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        pars = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]

        def find(node):
            if node == pars[node]:
                return pars[node]
            pars[node] = find(pars[node])
            return pars[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                pars[p2], pars[n2] = p1, p1
                rank[p1] += rank[p2]

            else:
                pars[p1], pars[n1] = p2, p2
                rank[p2] += rank[p1]
            return True

        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if not union(n1, n2):
                return edge