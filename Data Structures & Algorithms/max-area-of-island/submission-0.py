class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        i could loop through the grid
        if the current position is 0, keep moving 
        if the current position is 1, increment count
        check all directions for 1, increment count and update max_count
        seen = grid seen
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        res = 0
        count = 0

        def dfs(r, c):
            if (r < 0 or r >= ROWS 
                or c < 0 or c >= COLS
                or (r, c) in seen
                or grid[r][c] == 0):
                return 0

            seen.add((r, c))
            return 1 + (dfs(r + 1,c) +
                    dfs(r - 1, c) 
                    + dfs(r, c + 1)
                    + dfs(r, c - 1))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    res = max(res, dfs(r, c))
        return res