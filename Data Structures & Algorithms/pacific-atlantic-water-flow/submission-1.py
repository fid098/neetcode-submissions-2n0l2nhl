class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()
        a_que = deque()
        a_seen = set()

        ROWS, COLS = len(heights), len(heights[0])

      #add top to queue
        for i in range(COLS):
            p_que.append((0, i))
            p_seen.add((0, i))

        #add left to queue
        for i in range(1, ROWS):
            p_que.append((i, 0))
            p_seen.add((i, 0))

        #add bottom to queue 
        for i in range(COLS):
            a_que.append((ROWS - 1, i))
            a_seen.add((ROWS - 1, i))

        #add right to queue 
        for i in range(ROWS - 1):
            a_que.append((i, COLS - 1))
            a_seen.add((i, COLS - 1))

        
        #find neighbours that reach edges
        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i, j))
                for i_off, j_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r = i + i_off
                    c = j + j_off
                    if (r < 0 or r >= ROWS
                        or c < 0 or c >= COLS
                        or (r, c) in seen
                        or heights[r][c] < heights[i][j]):
                        continue
                    seen.add((r, c))
                    que.append((r, c))
            return coords

        a_coords = get_coords(a_que, a_seen)
        p_coords = get_coords(p_que, p_seen)

        return list(a_coords.intersection(p_coords))
