class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pars = [i for i in range(n)]
        ranks = [1 for i in range(n)]
        
        def find(node):
            if node == pars[node]:
                return node
            pars[node] = find(pars[node])
            return pars[node]
        
        def union(p1, p2):
            r1, r2 = ranks[p1], ranks[p2]
            if r1>r2:
                r1+=r2
                pars[p2] = p1
            else:
                r2+=r1
                pars[p1] = p2

        for first, second in edges:
            p1, p2 = find(first), find(second)
            union(p1, p2)
        
        s = set()
        for par in pars:
            s.add(find(par))
        return len(s)
