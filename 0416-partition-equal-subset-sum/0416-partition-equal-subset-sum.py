class Solution:
    def part(self,nums,index,part_sum1,part_sum2,dp):
        if dp[index][part_sum1]!=-1:
            return dp[index][part_sum1]
        if index==-1: 
            return part_sum1==part_sum2
        else :
            dp[index-1][part_sum1+nums[index]]=self.part(nums,index-1,part_sum1+nums[index],part_sum2,dp)
            dp[index-1][part_sum1]=self.part(nums,index-1,part_sum1,part_sum2+nums[index],dp)
            return dp[index-1][part_sum1+nums[index]] or dp[index-1][part_sum1]
        return false
        
    def canPartition(self, nums: List[int]) -> bool:
        dp=[[-1]*(sum(nums)+1) for _ in range(0,len(nums))]
        return self.part(nums,len(nums)-2,0,nums[-1],dp)