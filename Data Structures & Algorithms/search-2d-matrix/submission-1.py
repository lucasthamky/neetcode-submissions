class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        column = len(matrix[0])
        for n in range(len(matrix)):
            if matrix[n][column - 1] < target:
                continue
                
            if matrix[n][column - 1] >= target:
                for i in range(len(matrix[n])):
                    if matrix[n][i] == target:
                        result = True
                        break
                    else:
                        continue
            
        return result
                    

    

                

        