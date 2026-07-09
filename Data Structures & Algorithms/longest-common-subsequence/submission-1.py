class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = defaultdict(int)
        def dfs(text1, text2):
            if text1 == text2:
                return len(text1)
            if not text1 or not text2:
                return 0

            if (len(text1), len(text2)) in memo:
                return memo[(len(text1), len(text2))]
            
            if text1[0] == text2[0]:
                memo[(len(text1), len(text2))] = 1 + dfs(text1[1:], text2[1:])
            else:
                memo[(len(text1), len(text2))] = max(dfs(text1[1:], text2), dfs(text1, text2[1:]))
            
            return memo[(len(text1), len(text2))]
        
        return dfs(text1, text2)