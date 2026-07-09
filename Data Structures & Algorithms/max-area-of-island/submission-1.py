class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()
        res = 0

        def dfs(row, col):
            if (row, col) in visited or row < 0 or row >= num_rows or col <0 or col >= num_cols or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            area = 1
            for r, c in directions:
                area += dfs(row+r, col+c)
            return area


        for row in range(num_rows):
            for col in range(num_cols):
                res = max(res, dfs(row, col))
        return res