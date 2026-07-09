class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for i in range(len(s))]



        for i in range(len(s)):
            for word in wordDict:
                l = len(word)
                if l <= i+1 and s[i-l+1:i+1] == word and (i-l+1 == 0 or memo[i-l]):
                    memo[i] = True
                    break
        
        return memo[-1]