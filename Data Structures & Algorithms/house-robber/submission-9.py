class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <3:
            return max(nums)
        rob1, rob2 = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            tmp = max(rob2, rob1+nums[i])
            rob1=rob2
            rob2=tmp
        return rob2