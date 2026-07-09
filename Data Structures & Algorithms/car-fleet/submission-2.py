class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in pairs:
            time = (target - p)/s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
            

# [0, 1]. [1, 2]. [4, 2]. [7, 1]