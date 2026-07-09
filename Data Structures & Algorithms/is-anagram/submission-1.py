class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_char = s[i]
            if s_char in s_hash:
                s_hash[s_char] += 1
            else:
                s_hash[s_char] = 1
            t_char = t[i]
            if t_char in t_hash:
                t_hash[t_char] += 1
            else:
                t_hash[t_char] = 1
        return s_hash == t_hash
