class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(helper(nums[0:len(nums)-1]), helper(nums[1:]))

