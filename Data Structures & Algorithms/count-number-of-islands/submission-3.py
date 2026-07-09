class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        visited = set()

        def dfs(row, col):
            if (row, col) in visited or row <0 or row>= num_rows or col<0 or col >= num_cols or grid[row][col] == "0":
                return
            visited.add((row, col))
            for r, c in directions:
                dfs(row+r, col+c)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    count +=1
                    dfs(row, col)

        return count