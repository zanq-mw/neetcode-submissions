class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                s = set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        if board[r][c] != "." and board[r][c] in s:
                            return False
                        s.add(board[r][c])

        for row in board:
            s = set()
            for num in row:
                if num != "." and num in s:
                    return False
                s.add(num)

        for col in range(9):
            s = set()
            for row in range(9):
                if board[row][col] != "." and board[row][col] in s:
                    return False
                s.add(board[row][col])

        return True
