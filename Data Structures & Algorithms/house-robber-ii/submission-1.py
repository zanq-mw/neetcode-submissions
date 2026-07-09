class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        rob1, rob2 = 0, 0
        for num in nums[1:]:
            tmp = max((num + rob1), rob2)
            rob1 = rob2
            rob2 = tmp
        
        rob3 = rob2

        rob1, rob2 = 0, 0
        for num in nums[0:len(nums)-1]:
            tmp = max((num + rob1), rob2)
            rob1 = rob2
            rob2 = tmp
        return max(rob3, rob2)