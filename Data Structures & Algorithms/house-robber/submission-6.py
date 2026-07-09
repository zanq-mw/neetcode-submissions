class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums)+1)]

        def dfs(nums):
            if len(nums) == 0:
                return 0

            if len(nums) == 1:
                return nums[0]

            if len(nums) == 2:
                return max(nums)

            if memo[len(nums)] != -1:
                return memo[len(nums)]
            
            
            first = nums[0]
            memo[len(nums)] = max(first + dfs(nums[2:]), dfs(nums[1:]))
            return memo[len(nums)]

        return dfs(nums)