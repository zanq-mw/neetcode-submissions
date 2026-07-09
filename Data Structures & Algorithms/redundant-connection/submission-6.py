class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pars = [i for i in range(len(edges)+1)]
        ranks = [1 for i in range(len(edges)+1)]

        def find(node):
            if pars[node] == node:
                return node
            pars[node] = find(pars[node])
            return pars[node]
        
        def union(p1, p2):
            if ranks[p1] > ranks[p2]:
                ranks[p1] += ranks[p2]
                pars[p2] = p1
            else:
                ranks[p2] += ranks[p1]
                pars[p1] = p2

        for n1, n2 in edges:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]
            union(p1, p2)