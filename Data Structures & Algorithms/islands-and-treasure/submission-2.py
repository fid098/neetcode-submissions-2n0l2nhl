class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])

        q = deque()
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        distance = 1
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if dr+r<0 or dr+r==row or dc+c<0 or dc+c==col or (dr+r, dc+c) in visited or grid[dr+r][dc+c] == -1:
                        continue
                    grid[dr+r][dc+c] = distance
                    visited.add((dr+r, dc+c))
                    q.append((dr+r, dc+c))
            distance +=1
        


            