class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1] 

        if rowIndex == 0:
            return prev_row

        else:
            for row in range(1, rowIndex + 1):
                if row < 2:
                    curr_row = [None] * (row + 1)
                    curr_row[0] = 1
                    curr_row [row] = 1 
                else: 
                    curr_row = [None] * (row + 1)
                    curr_row[0] = 1
                    curr_row [row] = 1                     
                for i in range(1, len(curr_row) - 1):
                    curr_row[i] = prev_row[i] + prev_row[i - 1]
            
                prev_row = curr_row

        return prev_row

                
