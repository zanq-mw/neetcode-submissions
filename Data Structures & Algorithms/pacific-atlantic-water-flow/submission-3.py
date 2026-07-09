class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        pacific = set()
        atlantic = set()

        def dfs(row, col, parent, visited):
            if (row, col) in visited or row < 0 or row >= num_rows or col < 0 or col >= num_cols or parent > heights[row][col]:
                return
            
            visited.add((row, col))
            for r, c in directions:
                nr, nc = row+r, col+c
                dfs(nr, nc, heights[row][col], visited)

        for r in range(num_rows):
            dfs(r, 0, 0, pacific)
            dfs(r, num_cols-1, 0, atlantic)

        for c in range(num_cols):
            dfs(0, c, 0, pacific)
            dfs(num_rows-1, c, 0, atlantic)

        res = []

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r,c])

        return res