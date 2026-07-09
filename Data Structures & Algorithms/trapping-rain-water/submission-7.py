class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        leftmax = [0 for i in range(n)]
        rightmax = [0 for i in range(n)]

        leftmax[0] = height[0]
        rightmax[-1] = height[-1]

        for i in range(1, n):
            leftmax[i] = max(height[i], leftmax[i-1])

        for i in range(n-2, -1, -1):
            rightmax[i] = max(height[i], rightmax[i+1])

        res = 0
        for i in range(n):
            res += min(leftmax[i], rightmax[i]) - height[i]

        return res