class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set()
        for word in wordDict:
            wordset.add(word)

        memo = [False for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[j:i+1] in wordset and (memo[j-1] or j == 0):
                    memo[i] = True
                    break
        return memo[-1]
