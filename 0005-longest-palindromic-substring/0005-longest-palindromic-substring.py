class Solution:
    def checkpalin(self,n,m,s):
        while n>=0 and m<len(s):
             if s[n]==s[m]:
                n-=1
                m+=1
             else:
                break
        return (n+1,m)


    def longestPalindrome(self, s: str) -> str:
        mx_st=0
        n_x=0
        m_x=0
        if len(s)<=1:
            return s
        for i in range(0,len(s)):
            n_1,m_1 =  self.checkpalin(i,i,s)

            n_2,m_2 =  self.checkpalin(i,i+1,s) 
        
            if m_2-n_2>m_x-n_x:
               n_x=n_2
               m_x=m_2
            elif m_1-n_1>m_x-n_x:
                n_x=n_1
                m_x=m_1

        return s[n_x:m_x]