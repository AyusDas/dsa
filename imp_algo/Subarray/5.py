"""
Given an array of integers 
nums and an integer k, return the total number of subarrays whose 
sum equals to k.
"""

def subarraySum(self, nums, k: int) -> int:
    count = 0
    pref = 0
    hmap = {0:1}
    for i in range(len(nums)):
        pref += nums[i]
        rem = pref - k
        count += hmap.get(rem,0)
        hmap[pref] = 1 + hmap.get(pref,0)
    return count