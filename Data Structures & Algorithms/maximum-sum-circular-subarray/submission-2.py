class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentsum = 0
        maxsum = nums[0]
        currentminsum = 0
        minsum = nums[0]
        for num in nums:
            currentsum = max(currentsum+num, num)
            currentminsum = min(currentminsum+num, num)
            maxsum = max(currentsum, maxsum)
            minsum = min(currentminsum, minsum)
        if minsum != sum(nums):
            return max(maxsum, sum(nums) - minsum)
        return maxsum

        