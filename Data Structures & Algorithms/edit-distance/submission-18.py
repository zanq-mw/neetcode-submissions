class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i+1, j+1)
                return memo[(i, j)]
            
            option1 = helper(i+1, j)
            option2 = helper(i, j+1)
            option3 = helper(i+1, j+1)
            memo[(i, j)] = 1+ min(option1, option2, option3)
            return memo[(i, j)]
        
        return helper(0, 0)



        # monkeys
        # money

        # eys, ey.  word1[i+1:] word2[j:]

        # keys, y.  word1[i:]. word2[j+1:]

        # eys, y.   word1[i+1:]. word2[j+1:]