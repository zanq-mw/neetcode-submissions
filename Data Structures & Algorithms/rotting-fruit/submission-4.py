class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        count = 0
        t = 0
        q = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    count +=1
                elif grid[row][col] == 2:
                    q.append((row, col))

        
        while q and count:
            t += 1
            qlen = len(q)
            for _ in range(qlen):
                row, col = q.popleft()
                for r, c in directions:
                    nr, nc = row+r, col +c
                    if nr not in range(num_rows) or nc not in range(num_cols) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    count -= 1
                    q.append((nr, nc))
        
        return t if count == 0 else -1