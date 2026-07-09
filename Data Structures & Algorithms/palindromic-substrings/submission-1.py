class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1
            for j in range(i-1, -1, -1):
                stop = j-1 if j > 0 else None
                if s[j] == s[i] and s[j:i+1] == s[i:stop:-1]:
                    count+=1
        return count