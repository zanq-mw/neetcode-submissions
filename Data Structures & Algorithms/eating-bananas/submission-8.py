class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r

        while l < r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            # if total == h:
            #     return mid
            if total <= h:
                res = mid
                r = mid
            else:
                l = mid + 1

        return res