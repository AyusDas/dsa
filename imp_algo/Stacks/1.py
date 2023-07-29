"""
finding the next greater element in array for all indices
time : O(n)
"""

def nge(nums):
    stack = []
    ans = [-1 for _ in range(len(nums))]
    i = 0
    while i < len(nums):
        if len(stack) == 0:
            stack.append(i)
            i += 1 
            continue
        while len(stack) != 0 and nums[stack[-1]] < nums[i]:
            ans[stack[-1]] = nums[i]
            stack.pop()
        stack.append(i)
        i += 1
    return ans 