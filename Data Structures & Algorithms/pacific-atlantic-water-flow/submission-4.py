class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        num_rows = len(heights)
        num_cols = len(heights[0])

        pvisited = set()
        avisited = set()
        pac = set()
        atl = set()

        def dfs(row, col, prev, visited, bank):
            if row not in range(num_rows) or col not in range(num_cols) or (row, col) in visited or heights[row][col] < prev:
                return
            visited.add((row, col))
            for r, c in directions:
                dfs(row+r, col+c, heights[row][col], visited, bank)


        for row in range(num_rows):
            dfs(row, 0, 0, pvisited, pac)
            dfs(row, num_cols-1, 0, avisited, atl)

        for col in range(num_cols):
            dfs(0, col, 0, pvisited, pac)
            dfs(num_rows-1, col, 0, avisited, atl)

        res = []

        for coord in pvisited: 
            if coord in avisited:
                res.append([coord[0], coord[1]])

        return res