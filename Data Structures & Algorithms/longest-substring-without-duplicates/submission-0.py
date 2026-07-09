class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        result = 1
        l, r = 0, 1
        dic = {s[0]: 0}

        while r < len(s):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            
            if (r - l) + 1 > result:
                result = r-l + 1
            
            dic[s[r]] = r
            r += 1

        return result

