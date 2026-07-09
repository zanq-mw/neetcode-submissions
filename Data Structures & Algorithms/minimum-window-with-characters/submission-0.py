class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        have = 0
        needs_count = defaultdict(int)
        haves_count = {}
        for c in t:
            needs_count[c] +=1
            haves_count[c] = 0
        need = len(needs_count)

        res = [0, 0]
        res_len = len(s)+1
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            if c in haves_count:
                haves_count[c] += 1
                if haves_count[c] == needs_count[c]:
                    have +=1
            while have == need:
                if r-l +1 < res_len:
                    res_len = r-l+1
                    res = [l,r]
                if s[l] in haves_count:
                    haves_count[s[l]] -=1
                    if haves_count[s[l]] < needs_count[s[l]]:
                        have -=1
                l+=1
            r+=1

        if res_len == len(s)+1:
            return ""
        
        l, r = res
        return s[l:r+1]

