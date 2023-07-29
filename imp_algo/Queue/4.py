"""
leetcode 1696: Jump game 6 
"""
import collections
def maxResult(self, nums, k: int) -> int:
    q = collections.deque()
    N = len(nums)
    dp = [0 for i in range(N)]
    dp[N-1] = nums[N-1]
    q.append(N-1)
    for i in range(N-2,-1,-1):
        if q[0]-i > k : q.popleft()
        dp[i] = nums[i] + dp[q[0]]
        while len(q) and dp[q[-1]] < dp[i] : q.pop()
        q.append(i)
    return dp[0]