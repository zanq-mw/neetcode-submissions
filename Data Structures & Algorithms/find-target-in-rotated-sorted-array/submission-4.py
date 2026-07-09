class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2  
            print(mid)
            if target == nums[mid]:
                return mid
            elif nums[mid] > nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid
                elif target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                else:
                    return -1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                elif target < nums[mid] or target >= nums[l]:
                    r = mid
                else:
                    print("WAYYY")
                    return -1
        if nums[l] == target:
            return l
        else: 
            return -1