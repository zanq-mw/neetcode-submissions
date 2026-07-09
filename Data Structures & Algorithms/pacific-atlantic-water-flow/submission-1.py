class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, col, ocean, prev):
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return
            if (row, col) in ocean:
                return
            if heights[row][col] >= prev:
                ocean.add((row, col))
                for r, c in directions:
                    new_r, new_c = row + r, col + c
                    dfs(new_r, new_c, ocean, heights[row][col])

        for row in range(num_rows):
            dfs(row, 0, pacific, -1)
            dfs(row, num_cols-1, atlantic, -1)

        for col in range(num_cols):
            dfs(0, col, pacific, -1)
            dfs(num_rows-1, col, atlantic, -1)

        result = []


        for coord in pacific:
            if coord in atlantic:
                result.append(coord)

        return result