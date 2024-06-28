class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num_ls1=version1.split('.')
        num_ls2=version2.split('.')
        p=len(num_ls1)
        q=len(num_ls2)
        for i in range(0,max(len(num_ls1),len(num_ls2))):
            if(i<p):
              n=int(num_ls1[i])
            else:
              n=0
            if(i<q):
              m=int(num_ls2[i])
            else:
              m=0
            print(f"{n}  {m} ")
            if n>m:
               return 1
            elif n<m:
                return -1
        return 0