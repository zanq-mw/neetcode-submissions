class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(int)
        def dfs(i, j):
            if i>= len(word1):
                return len(word2) - j
            if j>= len(word2):
                return len(word1)-i

            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                o1 = dfs(i+1, j+1)
                o2 = dfs(i, j+1)
                o3 = dfs(i+1, j)
                memo[(i, j)] = 1 + min([o1, o2, o3])
            return memo[(i, j)]
        
        return dfs(0, 0)

        # keys
        # ey

        # eys  word1[1:]
        # y.   word2[1:]

        # eys. word1[1:]
        # ey.  word2

        # keys word1
        # y.   word2[1:]