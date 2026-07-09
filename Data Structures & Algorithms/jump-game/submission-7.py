class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums)-1:
            # if i == len(nums) -1:
            #     return True
            if nums[i] == 0:
                return False

            if i + nums[i] >= len(nums)-1:
                i += nums[i]
            else:
                temp = 0
                new_i = 0
                
                for j in range(i+1, i + nums[i] + 1):
                    if nums[j] + j > temp:
                        temp = nums[j] + j
                        new_i = j
                
                i = new_i
        return True