"""
No. of longest increases in an array
time: O(n^2)
"""

def findNumberOfLIS(nums) -> int:
    n = len(nums)
    dp = [[1, 1] for _ in range(n)]
    max_length = 0
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j][0] + 1 > dp[i][0]:
                    dp[i] = [dp[j][0] + 1, dp[j][1]]
                elif dp[j][0] + 1 == dp[i][0]:
                    dp[i][1] = dp[i][1] + dp[j][1]
        max_length = max(max_length, dp[i][0])
    res = 0
    for idx, (length, cnt) in enumerate(dp):
        if length == max_length:
            res += cnt
    return res