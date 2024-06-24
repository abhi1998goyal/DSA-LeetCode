class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if len(strs[0])<=0:
            return ""
        s1=strs[0]
        min_s=inf
        for s in range(1,len(strs)):
            x=0
            for i in range(0,min(len(s1),len(strs[s]))):
                if s1[i] == strs[s][i]:
                   x+=1
                else :
                   break
            print(x)
            min_s=min(x,min_s)
        return strs[0][:min_s]
                   

        