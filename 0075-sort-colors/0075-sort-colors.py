class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=mid=0
        n=len(nums)
        high=n-1
        while mid<=high:
            if nums[mid]==0:
               nums[mid]=nums[low]
               nums[low]=0
               #nums[mid]=1
               mid+=1
               low+=1
            elif nums[mid]==1:
                 mid+=1
            elif nums[mid]==2:
                 nums[mid]=nums[high]
                 nums[high]=2
                 high-=1

        print(f'low {low} ')
        print(f'high {high} ')
        print(f'mid {mid}')


        