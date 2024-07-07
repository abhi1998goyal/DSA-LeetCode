class Solution:
    def pathSum(self,grid,cord,n,m,dp):
        x=cord[0]
        y=cord[1]
        if x>n-1 or y>m-1:
            return inf

        if dp[x][y]!=-1:
            return dp[x][y]
        
        if x==n-1 and y==m-1:
            return grid[x][y]
        
        dp[x][y]=min(grid[x][y]+self.pathSum(grid,(x+1,y),n,m,dp),grid[x][y]+self.pathSum(grid,(x,y+1),n,m,dp) )
        return dp[x][y]
    

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[-1]*len(grid[0]) for _ in range(len(grid))]
        return self.pathSum(grid,(0,0),len(grid),len(grid[0]),dp)