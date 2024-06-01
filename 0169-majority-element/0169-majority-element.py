class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr=nums[0]
        nu=1
        for i in range(1,len(nums)): 
            if(curr==nums[i]):
                nu+=1
            else:
                nu-=1
                if(nu<=0):
                    curr=nums[i]
                    nu=1
        return curr