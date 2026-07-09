class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in nums:
            if num-1 not in numset:
                count = 1
                nxt = num+1
                while nxt in numset:
                    count+=1
                    nxt+=1
                res = max(count, res)

        return res