class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        pars = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            parent = pars[node]
            if node == parent:
                return parent
            parent = find(parent)
            pars[node] = parent
            return parent

        def union(p1, p2):
            if rank[p1] > rank[p2]:
                pars[p2] = p1
                rank[p1] += rank[p2]
            else:
                pars[p1] = p2
                rank[p2] += rank[p1]
        
        for edge in edges:

            p1 = find(edge[0])
            p2 = find(edge[1])
            if p1 != p2:
                union(p1, p2)
        result = set()
        for par in pars:
            result.add(find(par))

        return len(result)
        

