class Solution:
    def lcs(self,t1,t2,n,m,dp):
        if n>=len(t1) or m>=len(t2):
            return 0
        if dp[n][m]!=-1:
            return dp[n][m]
        if t1[n]==t2[m]:
            dp[n][m] = 1+self.lcs(t1,t2,n+1,m+1,dp)
            return dp[n][m]
        else :
            dp[n][m]= max(self.lcs(t1,t2,n+1,m,dp),self.lcs(t1,t2,n,m+1,dp))
            return dp[n][m]
        return 0

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*len(text2) for _ in range(len(text1))]
        return self.lcs(text1,text2,0,0,dp)