class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s) or len(s) == 1:
            return len(s)

        def letter_to_index(c: str) -> int:
            """
            Map an uppercase letter A-Z to 0-25.
            Raises ValueError if input is not A-Z.
            """
            c = c.upper()
            if not ('A' <= c <= 'Z'):
                raise ValueError("Input must be a letter A-Z")
            return ord(c) - ord('A')

        l,r = 0,0
        lst = [0 for _ in range(26)]
        count = 0
        while r<len(s):
            lst[letter_to_index(s[r])] +=1
            if max(lst) + k >= sum(lst):
                count = max(count, sum(lst))
                r+=1
            else:
                while max(lst) + k < sum(lst) and l<r:
                    lst[letter_to_index(s[l])] -=1
                    l+=1
                r+=1

        return count