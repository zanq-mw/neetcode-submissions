class Solution:
    def numDecodings(self, s: str) -> int:
        # memo = [-1 for _ in range(len(s))]
        decode1, decode2 = 1, 1

        def isValid(n):
            if n[0] == "0":
                return False
            n = int(n)
            return n > 0 and n < 27

        if not s or not isValid(s[0]):
            return 0

        for i in range(1, len(s)):
            tmp = 0
            if isValid(s[i]):
                tmp += decode2
            if isValid(s[i-1:i+1]):
                tmp += decode1
            if tmp == 0:
                return 0
            decode1 = decode2
            decode2 = tmp

        return decode2

