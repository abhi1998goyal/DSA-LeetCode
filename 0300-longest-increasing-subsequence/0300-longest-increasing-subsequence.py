from typing import List

class Solution:
    def lis(self, last_index, curr_index, nums,dp):   

        if -1<last_index and last_index<len(nums) and -1<curr_index and curr_index<len(nums) and dp[last_index][curr_index]!=-1 : 
            return dp[last_index][curr_index]

        if curr_index >= len(nums):
            return 0      
        if last_index == -1:
            result = max(self.lis(curr_index, curr_index + 1, nums,dp) + 1, self.lis(-1, curr_index + 1, nums,dp))
        
        elif nums[curr_index] <= nums[last_index]:
            result = self.lis(last_index, curr_index + 1, nums,dp)
        else:
            result = max(1 + self.lis(curr_index, curr_index + 1, nums,dp),self.lis(last_index, curr_index + 1, nums,dp))
        
        if last_index!=-1 or curr_index>=len(nums):
           dp[last_index][curr_index]=result
        return result

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[[-1]*len(nums) for _ in range(len(nums))]
        return self.lis(-1, 0, nums,dp)