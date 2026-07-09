class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dic:
                dic[num].append(i)
            else:
                dic[num] = [i]

        for key in dic:
            second = target - key
            if second == key:
                if len(dic[key]) == 2:
                    return dic[key] 
            elif second in dic:
                print(dic)
                return [dic[key][0], dic[second][0]]
