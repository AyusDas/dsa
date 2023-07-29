"""
Given an integer array nums, find a 
subarray that has the largest product, and return the product.
"""

def maxProduct(self, nums) -> int:
    maxi = float('-inf')
    pref = 1
    suff = 1
    for i in range(len(nums)):
        if pref == 0 : pref = 1
        if suff == 0 : suff = 1
        pref *= nums[i]
        suff *= nums[len(nums)-i-1]
        maxi = max(maxi,pref,suff)
    return maxi