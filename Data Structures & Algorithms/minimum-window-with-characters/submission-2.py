class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have_dict = {}
        have = 0
        need_dict = defaultdict(int)
        for c in t:
            have_dict[c] = 0
            need_dict[c] += 1
        need = len(need_dict)

        if len(s) < len(t):
            return ""

        l, r = 0, 0

        res = ""
        res_len = 1001

        while r < len(s):
            c = s[r]
            if c in have_dict:
                have_dict[c] +=1
                if have_dict[c] == need_dict[c]:
                    have += 1
            while have == need:
                if r-l+1 < res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                if s[l] in have_dict:
                    have_dict[s[l]] -=1
                    if have_dict[s[l]] < need_dict[s[l]]:
                        have -= 1
                l+=1
            r+=1
        return res