class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        

        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                if num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and r>l:
                        l+=1
                elif num + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
        
        return res