class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix) ,len(matrix[0])
        top_row,bot_row = 0 , ROWS-1

        # first figure out which row

        while (top_row <= bot_row):
            row = (top_row + bot_row) // 2
            if (target > matrix[row][-1]):
                top_row = row + 1
            elif (target < matrix[row][0]):
                bot_row = row -1
            else:
                break

        # if in case row wasnt found and exit

        if not (top_row <= bot_row):
            return False
        
        row = (top_row + bot_row) // 2

        l ,r = 0 , COLS - 1

        while(l <= r):
            mid = (l + r) // 2
            if (target > matrix[row][mid]):
                l = mid + 1
            elif (target < matrix[row][mid]):
                r = mid - 1
            else :
                return True
        
        # incase the target wasnt found in the specific row
        return False
        