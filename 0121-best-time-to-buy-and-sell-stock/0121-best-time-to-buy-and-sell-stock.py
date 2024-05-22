class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
            
        prices2=[]
        for i in range(1,len(prices)):
            prices2.append(prices[i]-prices[i-1])

        dp=[prices2[0]]
        mx=dp[0]
        for j in range(1,len(prices2)):
            dp.append(max(prices2[j],dp[j-1]+prices2[j]))
            mx=max(dp[-1],mx)
        if mx<0:
           mx=0
        return mx

        

