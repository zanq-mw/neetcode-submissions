class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        has_zero = False
        for num in nums:
            if num == 0:
                if has_zero:
                    return [0 for _ in range(len(nums))]
                else:
                    has_zero = True
                continue
            total = total * num

        result = []
        for num in nums:
            if num != 0:
                if has_zero:
                    result.append(0)
                else:
                    result.append(int(total/num))
            else:
                result.append(total)
        return result