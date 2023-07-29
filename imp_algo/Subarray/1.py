"""
maximum sum subarray or kadanes algo
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
"""
def maxSubArray(self, nums) -> int:
    maxi = nums[0]
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        maxi = max(maxi,s)
        if s < 0 : s = 0
    return maxi  