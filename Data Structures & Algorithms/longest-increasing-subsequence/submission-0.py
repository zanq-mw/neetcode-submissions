class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            for j, n in enumerate(nums[0:i]):
                if num > n:
                    lis[i] = max(lis[i], 1 + lis[j])
        
        print(lis)
        return max(lis)
