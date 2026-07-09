class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)+1
        l = 1
        res = r

        while l<r:
            m = (l+r)//2
            total = 0
            for p in piles:
                total += math.ceil(p/m)
            if total<=h:
                res = m
                r = m
            else:
                l=m+1
        return res