class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        if len(matrix) == 1 and len(matrix[0]) ==1:
            return [matrix[0][0]]
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            res = []
            for row in matrix:
                res.append(row[0])
            return res
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        res = []
        for num in matrix[0]:
            res.append(num)
        
        for row in range(1, num_rows):
            res.append(matrix[row][-1])

        for col in range(num_cols-2, -1, -1):
            res.append(matrix[-1][col])

        for row in range(num_rows-2, 0, -1):
            res.append(matrix[row][0])
        
        new = []
        for i in range(1, num_rows-1):
            new.append(matrix[i][1:-1])

        if new and new[0]:
            res.extend(self.spiralOrder(new))
        return res

        