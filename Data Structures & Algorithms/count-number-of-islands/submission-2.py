class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        num_rows = len(grid)
        num_cols = len(grid[0])

       
        count = 0

        def bfs(row, col):
            grid[row][col] = "0"
            q = deque()
            q.append((row, col))
            while q:
            
                r, c = q.popleft()
                for r1, c1 in directions:
                    nr, nc = r+r1, c+c1
                    if nr <0 or nc < 0 or nr>= num_rows or nc >= num_cols or grid[nr][nc] == "0":
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))


        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "0":
                    continue
                count += 1
                bfs(row, col)

        return count