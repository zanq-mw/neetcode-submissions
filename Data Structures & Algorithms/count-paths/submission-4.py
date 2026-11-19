class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]

        memo[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    memo[i][j] += memo[i-1][j]
                if j > 0:
                    memo[i][j] += memo[i][j-1]
        return memo[-1][-1]