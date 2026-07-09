class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        extra = False

        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        extra = True
                    else:
                        matrix[row][0] = 0

        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(num_rows):
                matrix[row][0] = 0
        
        if extra:
            for col in range(num_cols):
                matrix[0][col] = 0
        