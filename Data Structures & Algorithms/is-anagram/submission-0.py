class Solution:
    def updateDic(self, dic, char):
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
        return dic

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            self.updateDic(dic1, s[i])
            self.updateDic(dic2, t[i])
        return dic1 == dic2
        