class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = collections.deque()

        def dfs(r, c):
            if (r<0 or c <0 or r>= num_rows or c>= num_cols or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res