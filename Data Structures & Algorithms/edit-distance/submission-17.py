class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(word1, word2):
            if not word1:
                return len(word2)
            if not word2:
                return len(word1)

            if (word1, word2) in memo:
                return memo[(word1, word2)]

            if word1[0] == word2[0]:
                memo[(word1, word2)] = helper(word1[1:], word2[1:])
                return memo[(word1, word2)]
            
            option1 = helper(word1[1:], word2)
            option2 = helper(word1, word2[1:])
            option3 = helper(word1[1:], word2[1:])
            memo[(word1, word2)] = 1+ min(option1, option2, option3)
            return memo[(word1, word2)]
        
        return helper(word1, word2)



        # monkeys
        # money

        # eys, ey.  word1[i+1:] word2[j:]

        # keys, y.  word1[i:]. word2[j+1:]

        # eys, y.   word1[i+1:]. word2[j+1:]