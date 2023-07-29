"""
finding the length of the longest subsequence such that the elements of the 
subsequence are in arithmetic progression
time : O(n^2)
"""

def func(nums):
    dp = {}
    for r in range(len(nums)):
        for l in range(0, r):
            dp[(r, nums[r] - nums[l])] = dp.get((l, nums[r] - nums[l]), 1) + 1   
    return max(dp.values())
