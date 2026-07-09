class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            for j in range(i):
                if num>nums[j]:
                    memo[i]= max(memo[i], 1+ memo[j])
        return max(memo)