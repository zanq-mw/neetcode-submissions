class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return []

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        num_rows = len(heights)
        num_cols = len(heights[0])

        atlantic_hash = set()
        pacific_hash = set()

        def dfs(r, c, visited, prev_height):
            if (r<0 or c <0 or r>= num_rows or c>= num_cols or heights[r][c] < prev_height) or (r,c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])

        for r in range(num_rows):
            for c in range(num_cols):
                if r == 0 or c == 0:
                    dfs(r, c, pacific_hash, 0)
                if r == num_rows -1 or c == num_cols -1:
                    dfs(r, c, atlantic_hash, 0)

        for r in range(num_rows):
            for c in range(num_cols):
                if (r,c) in atlantic_hash and (r,c) in pacific_hash:
                    res.append([r, c])

        return res