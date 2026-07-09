class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.add_word(word)

        num_rows = len(board)
        num_cols = len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        res = set()

        def dfs(row, col, curr, word):
            if row not in range(num_rows) or col not in range(num_cols) or (row, col) in visited or board[row][col] not in curr.children:
                return
            visited.add((row, col))
            curr = curr.children[board[row][col]]
            word += board[row][col]
            if curr.endOfWord:
                res.add(word)
            for r, c in directions:
                dfs(row+r, col+c, curr, word)

            visited.remove((row, col))

        for row in range(num_rows):
            for col in range(num_cols):
                dfs(row, col, trie, "")

        return list(res)