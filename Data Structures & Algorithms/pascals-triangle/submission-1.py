class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [None] * numRows

        for i in range(len(arr)):
            arr[i] = [None] * (i + 1)
            for j in range(len(arr[i])):
                if j == 0 or j == len(arr[i]) - 1:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]


        
        return arr



        