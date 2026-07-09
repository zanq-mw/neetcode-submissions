class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                tmp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(dfs(nums[0:-1]), dfs(nums[1:]))