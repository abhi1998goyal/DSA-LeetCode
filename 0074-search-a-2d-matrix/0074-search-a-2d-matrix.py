class Solution:
    @staticmethod
    def searchBinary(matrix, target, left, right, row,col):
        if left > right:
            return False
        
        mid = (left + right) // 2
        mid_value = matrix[mid // col][mid % col]
        
        if mid_value == target:
            return True
        elif mid_value > target:
            return Solution.searchBinary(matrix, target, left, mid - 1, row, col)
        else:
            return Solution.searchBinary(matrix, target, mid + 1, right, row, col)
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        row=len(matrix)
        col=len(matrix[0])
        right=row*col-1
       # print(right)
        return Solution.searchBinary(matrix,target,left,right,row,col)
        