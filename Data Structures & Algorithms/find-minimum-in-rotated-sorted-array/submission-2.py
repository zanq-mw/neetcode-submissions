class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        output=1001
        while l<=r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l=m+1
                # output = min(r, output)
            else:
                output = min(nums[m], output)
                r=m-1
        return output