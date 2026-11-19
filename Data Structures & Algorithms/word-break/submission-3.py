class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[j:i+1] in wordDict:
                    if j == 0 or memo[j-1]:
                        memo[i] = True

        return memo[-1]