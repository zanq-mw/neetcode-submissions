class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        count = 0

        while goal!=0:
            candidate = -1
            for i in range(goal-1,-1,-1):
                if i+nums[i] >= goal:
                    candidate = i
            if candidate == -1:
                return False
            count+=1
            goal=candidate
        return count