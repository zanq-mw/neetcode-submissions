class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        has_zero = False
        for num in nums:
            if num != 0:
                total = total * num
            elif has_zero:
                result = []
                for _ in nums:
                    result.append(0)
                return result
            else:
                has_zero = True
        result = []
        for num in nums:
            if num == 0:
                result.append(total)
            elif has_zero:
                result.append(0)
            else:
                result.append(int(total/num))

        return result

        