"""
finding the LIS in the array
Time : O(nlogn)
"""
from bisect import bisect_left
def func(nums):
    stack = []
    for i in range(len(nums)):
        if len(stack) == 0:
            stack.append(nums[i])
            continue
        if nums[i] > stack[-1]:
            stack.append(nums[i])
        else:
            idx = bisect_left(stack,nums[i])
            stack[idx] = nums[i]
    return len(stack)
