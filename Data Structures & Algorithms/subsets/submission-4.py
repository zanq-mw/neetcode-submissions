class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtracker(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtracker(i+1)

            subset.pop()
            backtracker(i+1)

        backtracker(0)
        return res