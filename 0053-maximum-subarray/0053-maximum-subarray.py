class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_far=0
        max_till=-inf
        for i in range(0,len(nums)):
            max_far=max_far+nums[i]
            if(max_till<max_far):
                max_till=max_far
            if(max_far<0):
                max_far=0
        return max_till

