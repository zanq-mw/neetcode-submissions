class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        result = n
        while result not in s:
            if result ==1:
                return True
            s.add(result)
            tmp = 0
            for c in str(result):
                tmp+= int(c) * int(c)
            result = tmp
        return False