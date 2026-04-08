class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        we want to iterate through every single letter in the board
        then check its adjacent neighbours if the next letter is in the word
        """

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            #we take the current row, column of the board and the index of the word
            if i == len(word):
                return True
            
            #edge cases: r and c out of bounds,
            #current word letter not the same as current position,
            #and position already in the path
            if (r < 0 or 
                c < 0 or
                r >= ROWS or
                c >= COLS or
                word[i] != board[r][c] or
                (r,c) in path):
                return False

            #we add the path
            #check the adjecent neighbours
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))

            #remove the position to backtrack
            path.remove((r,c))
            return res

        #iterate through
        for r in range(ROWS):
            for c in range(COLS):
                if (dfs(r, c, 0)):
                    return True
        return False 





