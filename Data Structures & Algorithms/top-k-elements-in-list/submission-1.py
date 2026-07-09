class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        dic = {}
        for i in range(len(nums)):
            dic[i+1] = []

        for key in count:
            n = count[key]
            dic[n].append(key)

        key = len(nums)
        output = []
        while len(output) < k and key != 0:

            if len(dic[key]) < 1:
                key -= 1
            else:
                pop = dic[key].pop()
                output.append(pop)

        return output