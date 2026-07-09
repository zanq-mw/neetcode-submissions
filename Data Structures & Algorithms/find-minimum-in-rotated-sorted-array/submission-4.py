class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                res = min(nums[m], res)  # potential minimum
                r = m - 1

        return res