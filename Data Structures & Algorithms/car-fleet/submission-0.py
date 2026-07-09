class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new = []
        for i, num in enumerate(position):
            new.append([num, (target-num)/speed[i]])
        
        data = sorted(new, key=lambda x: x[0], reverse=True)

        stack = []

        for d in data:
            if len(stack) > 0 and stack[-1][1] >= d[1]:
                continue
            else:
                stack.append(d)

        return len(stack)