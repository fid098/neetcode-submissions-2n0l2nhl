class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        count = 0
        seen = set()
        q = deque()

        def bfs():
            nonlocal fresh, count
            while q and fresh > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for i, j in [(1 , 0), (-1, 0), (0, 1), (0, -1)]:
                        new_r, new_c = r + i, c + j
                        if (new_r < 0 or new_r >= ROWS
                            or new_c < 0 or new_c >= COLS
                            or grid[new_r][new_c] != 1):
                            continue
                        #make it rotten 
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))
                count += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        bfs()
        return count if fresh == 0 else -1




