class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = []
        for i, num in enumerate(temperatures):
            output.append(0)
            while len(stack) > 0 and stack[-1][0] < num:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([num, i])
        return output