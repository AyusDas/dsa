"""
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

"""

def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
    buckets = {}
    w = t+1
    for i, num in enumerate(nums):
        bucket = num//w
        
        if bucket in buckets:
            return True
        else :
            buckets[bucket] = num
            if bucket-1 in buckets and num - buckets[bucket-1] <= t:
                return True
            if bucket+1 in buckets and buckets[bucket+1] - num <= t:
                return True
            if i >= k :
                del buckets[ nums[i-k]//w ]
    return False