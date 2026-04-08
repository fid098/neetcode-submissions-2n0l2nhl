class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        9 x 9 sudoku board 
        each row 1-9 without duplicates 
        each column 1-9 without duplicates 
        each of the nine 3x3 boxes 1-9 without duplicates
        return true if valid
        """

        rows = defaultdict(set)  #rows hashset with the row value as the key
        cols = defaultdict(set)   #cols hashet with the col value as the key
        squares = defaultdict(set) #sware hashset with the grid index as the key

        for i in range(9):   #for every row
            for j in range(9):   #for every column
                if board[i][j] == ".":   #if the current value is . continue
                    continue 
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3, j//3)]:
                    return False
                 
                #if the current value is in the row hashset, column hashset or the square hashset then it is not valid 

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
                #if it isnt then add the current value to the hashsets.
        return True


