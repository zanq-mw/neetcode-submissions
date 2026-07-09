class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        output = 0
        while l<r:
            height = min(heights[l], heights[r])
            length = r-l
            output = max(height*length, output)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return output