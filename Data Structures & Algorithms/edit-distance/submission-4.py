class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        def helper(word1, word2):
            if word1 == word2:
                return 0

            if not word1:
                return len(word2)
            
            if not word2:
                return len(word1)

            if memo[len(word1)][len(word2)] != -1:
                return memo[len(word1)][len(word2)]

            if word1[0] == word2[0]:
                memo[len(word1)][len(word2)] = helper(word1[1:], word2[1:])
                return memo[len(word1)][len(word2)]

            option1 = helper(word1[1:], word2)
            option2 = helper(word1, word2[1:])
            option3 = helper(word1[1:], word2[1:])

            memo[len(word1)][len(word2)] = 1+ min([option1, option2, option3])

            return memo[len(word1)][len(word2)]

        return helper(word1, word2)
        
#         monkeys
#         money

#         eys ey.  keys y.   eys y
    

#         eys ey.  keys y.  eys y

# word1[1:].   word1.       word1[1:]
# word2.       word2[1:].   word2[1:]