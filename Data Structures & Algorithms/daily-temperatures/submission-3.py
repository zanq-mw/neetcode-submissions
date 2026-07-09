class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, _ = stack.pop()
                result[index] = i-index
            stack.append([i, temperatures[i]])

        return result