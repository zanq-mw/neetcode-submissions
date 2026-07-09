class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * len(s)

        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        
        for i, char in enumerate(s):
            for j in range(i, -1, -1):
                if s[j:i+1] in wordSet and (j == 0 or memo[j-1]):
                    memo[i] = True
                    break
        return memo[-1]
        

