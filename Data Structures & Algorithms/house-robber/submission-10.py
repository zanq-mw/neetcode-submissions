class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums))]
        if len(nums) <3:
            return max(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[1], nums[0])

        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i-1), nums[i]+dfs(i-2))
            return memo[i]

        dfs(len(nums)-1)
        return memo[-1]