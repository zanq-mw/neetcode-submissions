class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            grid[row][col] = "0"
            for r, c in directions:
                nr, nc = row + r, col+c
                if nr in range(num_rows) and nc in range(num_cols) and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        
        return count

        