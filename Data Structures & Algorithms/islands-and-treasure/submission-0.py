class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[1, 0], [-1,0], [0, 1], [0, -1]]
        q = deque()
        count = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] ==0:
                    q.append((row, col, 0))
                elif grid[row][col] != -1:
                    count +=1

        while q and count >0:
            row, col, distance = q.popleft()
            # grid[row][col] = distance
            for r, c in directions:
                nr, nc = row+r, col+c
                if nr < 0 or nr>= num_rows or nc<0 or nc >= num_cols or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = distance + 1
                count -=1
                q.append((nr, nc, distance+1))


                

        