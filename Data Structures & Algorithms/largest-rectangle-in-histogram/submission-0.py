class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = [] # (start, height)
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                result = max(result, h * (index - i))
                start = i
            stack.append((start, height))

        for index, height in stack:
            result = max(result, height * (len(heights)-index))
        return result 