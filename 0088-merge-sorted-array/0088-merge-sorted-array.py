class Solution:
    @staticmethod
    def sorty(ls):
         ls.sort()
         return ls
        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
           left = m-1
           right =0
           while left>=0 and right<n:
                if nums1[left]>nums2[right]:
                    temp=nums1[left]
                    nums1[left]=nums2[right]
                    nums2[right]=temp
                    left-=1
                    right+=1
                else :
                    break
           
           print(nums1[0:m])
           nums1[0:m]=Solution.sorty(nums1[0:m])
           nums2.sort()

           nums1[m:]=nums2



        