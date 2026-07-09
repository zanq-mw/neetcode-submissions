class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(int)
        def dfs(word1, word2):
            if word1==word2:
                return 0
            if not word1:
                return len(word2)
            if not word2:
                return len(word1)
            if (len(word1), len(word2)) in memo:
                return memo[(len(word1), len(word2))]
            if word1[0] == word2[0]:
                memo[(len(word1), len(word2))] = dfs(word1[1:], word2[1:])
            else:
                o1 = dfs(word1[1:], word2[1:])
                o2 = dfs(word1, word2[1:])
                o3 = dfs(word1[1:], word2)
                memo[(len(word1), len(word2))] = 1 + min([o1, o2, o3])
            return memo[(len(word1), len(word2))]
        
        return dfs(word1, word2)

        # keys
        # ey

        # eys  word1[1:]
        # y.   word2[1:]

        # eys. word1[1:]
        # ey.  word2

        # keys word1
        # y.   word2[1:]