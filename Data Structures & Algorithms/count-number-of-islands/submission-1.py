class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        num_rows = len(grid)
        num_cols = len(grid[0])

        visited = set()
        count = 0

        def dfs(row, col):
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return
            if (row, col) in visited:
                return
            visited.add((row, col))
            if grid[row][col] == "1":
                for r, c in directions:
                    dfs(row + r, col + c)


        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in visited or grid[row][col] == "0":
                    continue
                count += 1
                dfs(row, col)

        return count