"""
Given an integer array nums and an integer k, return true if nums has a 
good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.

"""

def checkSubarraySum(self, nums, k: int) -> bool:
    rem = {0:-1}
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        r = total % k
        if r not in rem:
            rem[r] = i
        elif i - rem[r] > 1:
            return True
    return False