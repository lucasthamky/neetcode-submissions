class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        totalLength = row * col
        

        l, r = 0, totalLength-1
        while l <= r:
            m = (l + r) // 2

            cur_row = m // col
            cur_col = m % col
            print(l, r, cur_row, cur_col, m)

            if matrix[cur_row][cur_col] > target: 
                r = m - 1

            elif matrix[cur_row][cur_col] < target:
                l = m + 1
            
            else:
                return True
        
        return False
                

        