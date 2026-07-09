class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1, 0], [0, 1]]
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        memo[-1][-1] = 1

        def dfs(row, col):
            if row <0 or row >= m or col <0 or col>=n:
                return 0
            if memo[row][col] != -1:
                return memo[row][col]
            
            total = 0
            for r, c in directions:
                total += dfs(row+r, col+c)
            memo[row][col] = total
            return total

        return dfs(0, 0)