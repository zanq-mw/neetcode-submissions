class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]

        perms = self.permute(nums[1:])
        result = []
        for perm in perms:
            for i in range(len(perm)+1):
                p = perm.copy()
                p.insert(i, nums[0])
                result.append(p)

        return result