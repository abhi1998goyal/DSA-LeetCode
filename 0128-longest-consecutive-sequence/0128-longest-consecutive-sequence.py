class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_set={}
        max_cnt=0
        for i in range(0,len(nums)):
            uniq_set[nums[i]]=1
        for key in uniq_set:
            if key-1 in uniq_set:
                pass
            else:
                cnt=1
                while key+1 in uniq_set:
                    cnt+=1
                    key+=1
                if cnt>max_cnt:
                    max_cnt=cnt
        return max_cnt
            