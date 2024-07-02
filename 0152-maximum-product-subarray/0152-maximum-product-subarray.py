class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the neg_dp and pos_dp arrays
        neg_dp = [0] * len(nums)
        pos_dp = [0] * len(nums)
        
        # Initialize the first element of dp arrays
        if nums[0] < 0:
            neg_dp[0] = nums[0]
        else:
            pos_dp[0] = nums[0]
        
        # Initialize the maximum product with the first element
        mx_prod = nums[0]

        # Iterate through the array
        for i in range(1, len(nums)):
            if nums[i] < 0:
                pos_dp[i] = neg_dp[i-1] * nums[i]
                neg_dp[i] = pos_dp[i-1] * nums[i] if pos_dp[i-1] != 0 else nums[i]
            else:
                pos_dp[i] = pos_dp[i-1] * nums[i] if pos_dp[i-1] != 0 else nums[i]
                neg_dp[i] = neg_dp[i-1] * nums[i]

            # Update the maximum product
            mx_prod = max(mx_prod, pos_dp[i])

        return mx_prod
