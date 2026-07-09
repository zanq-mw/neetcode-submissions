class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dic:
                dic[num].append(i)
            else:
                dic[num] = [i]

        for num in nums:
            num2 = target - num
            if num != num2 and num2 in dic:
                return [dic[num][0], dic[num2][0]]

            if num == num2 and len(dic[num]) > 1:
                return [dic[num][0], dic[num][1]]