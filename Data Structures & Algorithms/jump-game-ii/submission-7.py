class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        count = 0

        while goal!=0:
            for i in range(0, goal):
                if i+nums[i] >= goal:
                    goal=i
                    count+=1
                    break
        return count