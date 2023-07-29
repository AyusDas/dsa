"""
finding the length of longest valid parenthesis in a string
time : O(n)
"""

def longestValidParentheses(self, s: str) -> int:
    dp = [0 for _ in range(len(s))]
    stack = []
    if len(s) < 2 :  return 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif len(stack) > 0:
            x = stack[-1]
            dp[i] = i - x + 1
            if x >= 1: dp[i] += dp[x-1]
            stack.pop()
        ans = max(ans,dp[i])
    return ans