class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(0,row):
            for j in range(0,col):
                if(i>j):
                   temp=matrix[i][j]
                   matrix[i][j]=matrix[j][i]
                   matrix[j][i]=temp
        

        for i in range(0,row):
            for j in range(0,col//2):
                   temp=matrix[i][j]
                   matrix[i][j]=matrix[i][col-1-j]
                   matrix[i][col-1-j]=temp