class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j]+1)
        
        return max(memo)