class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        given a m x n matrix and an integer target 
        each row is sorted in increasing order
        """

        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        #checks if we are on the right row
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break 

        if not (top <= bottom):
            return False
            
        #if we are on the right row, find the target
        row = (top + bottom) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True 
        return False
