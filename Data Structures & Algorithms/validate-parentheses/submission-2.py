class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif len(stack) > 0:
                pop = stack.pop()
                if pop == "(" and c != ")":
                    return False
                if pop == "[" and c != "]":
                    return False
                if pop == "{" and c != "}":
                    return False
            else:
                return False
        return len(stack) == 0
                