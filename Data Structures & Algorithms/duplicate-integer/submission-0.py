class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for val in nums:
            if val in dic:
                return True
            else:
                dic[val] = 1
        return False

        