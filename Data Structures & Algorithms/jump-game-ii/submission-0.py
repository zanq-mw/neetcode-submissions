class Solution:
    def jump(self, nums: List[int]) -> bool:
        i = 0
        count = 0
        while i < len(nums)-1:
            # if i == len(nums) -1:
            #     return True
            # if nums[i] == 0:
            #     return False

            if i + nums[i] >= len(nums)-1:
                return count + 1
            else:
                temp = 0
                new_i = 0
                
                for j in range(i+1, i + nums[i] + 1):
                    if nums[j] + j > temp:
                        temp = nums[j] + j
                        new_i = j
                count += 1
                i = new_i
        return count