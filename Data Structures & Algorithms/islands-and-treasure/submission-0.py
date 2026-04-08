class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        def addroom(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or grid[r][c] == -1):
                return
            q.append((r, c))
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):      # process entire level at once
                r, c = q.popleft()
                grid[r][c] = dist
                addroom(r + 1, c)
                addroom(r, c + 1)
                addroom(r - 1, c)
                addroom(r, c - 1)
            dist += 1

