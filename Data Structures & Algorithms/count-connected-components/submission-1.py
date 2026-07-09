class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if len(edges) >= n-1:
        #     return 1

        parents = []
        for i in range(n):
            parents.append(i)

        rank = [1] * n

        def find(node):
            print(node)
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        def union(n1, n2):
            print(n1, n2)
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    rank[p1] += rank[p2]
                    parents[p2] = parents[p1]
                else:
                    rank[p2] += rank[p1]
                    parents[p1] = parents[p2]
            
        for a, b in edges:
            union(a,b)
        result = set()
        for par in parents:
            result.add(find(par))
        return len(result)
