class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        if len(s) == 1:
            return 1
     
        memo = [0 for _ in range(len(s))]
        memo[0] = 1

        def isValid(num):
            if num[0] == "0":
                return False
            num = int(num)
            return num > 0 and num < 27

        if not isValid(s[0:2]) and not isValid(s[1]):
            return 0
        if int(s[1]) == 0 or not isValid(s[0:2]):
            memo[1] = 1
        else:
            memo[1] = 2

        for i in range(2, len(s)):
            single = s[i]
            double = s[i-1:i+1]
            if isValid(single):
                memo[i] += memo[i-1]
            if isValid(double):
                memo[i] += memo[i-2]

        return memo[-1]