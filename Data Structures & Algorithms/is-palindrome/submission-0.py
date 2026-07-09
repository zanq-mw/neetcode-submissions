class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.replace(" ", "").lower()
        s1 = "".join(filter(str.isalnum, s1))
        pointer = 0
        pointer2 = len(s1) - 1
        while pointer < pointer2:
            if s1[pointer] != s1[pointer2]:
                print([pointer, pointer2])
                return False
            pointer += 1
            pointer2 -= 1
        return True