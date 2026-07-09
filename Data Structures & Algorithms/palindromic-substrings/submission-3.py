class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        count = 0
        for i in range(len(s)):
            count += 1
            for j in range(i-1, -1, -1):
                stop = j-1 if j > 0 else None
                if s[j] == s[i] and (i-j<=2 or ((i-1, j+1) in memo and memo[(i-1, j+1)])):
                    count+=1
                    memo[(i, j)] = True
                else:
                    memo[(i, j)] = False

        return count