class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        
        l, r = 0, 0
        cache = defaultdict(int)
        maxf = 0
        res = 0

        while r<len(s):
            c = s[r]
            cache[c] += 1
            if cache[c] > maxf:
                maxf = cache[c]
            if maxf + k >= r-l+1:
                res = max(res, r-l+1)
            else:
                while maxf + k < r-l+1:
                    c = s[l]
                    cache[c] -= 1
                    # if maxchar ==c:
                    l+=1
            r+=1

        return res