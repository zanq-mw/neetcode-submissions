class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [-1 for _ in nums]
        memo2 = [-1 for _ in nums]

        def dfs(i, n, memo):
            if i >= n:
                return 0
            if memo[i] == -1:
                memo[i] = max(nums[i] + dfs(i+2, n, memo), dfs(i+1, n, memo))
            return memo[i]

        return max(dfs(0, len(nums)-1, memo), dfs(1, len(nums), memo2))

