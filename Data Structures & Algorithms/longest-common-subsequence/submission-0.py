class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = []
        for i in range(len(text1)):
            row = [-1 for _ in range(len(text2))]
            memo.append(row)

   

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            elif text1[i] == text2[j]:
                memo[i][j] = 1 + dfs(i-1, j-1)
                return memo[i][j]
            else:
                memo[i][j] = max(dfs(i-1, j), dfs(i, j-1))
                return memo[i][j]

        return dfs(len(text1)-1, len(text2)-1)
            