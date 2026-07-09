class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        count = 0

        q = deque()


        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    count+=1


        while q and count>0:
            len_q = len(q)
            for _ in range(len_q):
                row, col = q.popleft()
                for r, c in directions:
                    nr, nc = row+r, col+c
                    if nr in range(num_rows) and nc in range(num_cols) and grid[nr][nc] == 1:
                        count-=1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1

        if count > 0:
            return -1
        return time