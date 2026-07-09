class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        fresh = 0
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q= deque()

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        while q and fresh > 0:
            qlen = len(q)
            for i in range(qlen):
                row, col = q.popleft()
                for r, c in directions:
                    nr, nc = row + r, col + c
                    if nr < 0 or nc < 0 or nr >= num_rows or nc >= num_cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            time +=1

        return time if fresh == 0 else -1