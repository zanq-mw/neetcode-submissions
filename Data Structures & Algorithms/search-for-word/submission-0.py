class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def dfs(row, col, i):
            if i > len(word) - 1 or row not in range(num_rows) or col not in range(num_cols) or (row, col) in visited or board[row][col] != word[i]:
                return False
            if i == len(word) -1:
                return True
            visited.add((row, col))
            for r, c in directions:
                nr, nc = row+r, col+c
                if dfs(nr, nc, i+1):
                    visited.remove((row, col))
                    return True
            visited.remove((row, col))
            return False

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
            
