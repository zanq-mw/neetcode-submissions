class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()

        def dfs(row, col, i):
            if row not in range(num_rows) or col not in range(num_cols) or (row, col) in visited or board[row][col] != word[i]:
                return False
            if i == len(word)-1:
                return True
            visited.add((row, col))
            for r, c in directions:
                if dfs(row+r, col+c, i+1):
                    return True
            visited.remove((row, col))
            return False

        for row in range(num_rows):
            for col in range(num_cols):
                if dfs(row, col, 0):
                    return True
        return False