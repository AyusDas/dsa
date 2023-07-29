"""
finding the longest increasing subsequence ending in the ith index
time : O(n)
"""
def func(nums):
    dp = [-1 for i in range(len(nums))]
    def helper(i):
        ans = 1
        if dp[i] != -1:
            return dp[i]
        for j in range(i-1,-1,-1):
            if nums[j] < nums[i]:
                ans =  max(ans, 1 + helper(j))
        dp[i] = ans
        return dp[i]
