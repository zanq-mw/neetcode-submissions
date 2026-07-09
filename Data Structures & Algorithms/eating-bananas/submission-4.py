class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        result = max(piles)
        l = 1
        r = max(piles)
        while l<r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p/m)
            if total <= h:
                result = m
                r = m
            else:
                l = m+1

        return result