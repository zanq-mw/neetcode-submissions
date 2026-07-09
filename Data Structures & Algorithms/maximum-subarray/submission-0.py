class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = 0
        maxsum = nums[0]
        for num in nums:
            currentsum = max(currentsum+num, num)
            maxsum = max(currentsum, maxsum)

        return maxsum