class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col = len(matrix) , len(matrix[0])
        row_zero=[]
        col_zero=[]
        for i in range(0,row):
            for j in range(0,col):
                if(matrix[i][j]==0):
                    row_zero.append(i)
                    col_zero.append(j)

        for i in row_zero:
            for j in range(0,col):
                matrix[i][j]=0

        for i in range(0,row):
            for j in col_zero:
                matrix[i][j]=0

                
