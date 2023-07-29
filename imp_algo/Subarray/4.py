"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a 
subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

"""

def minSubArrayLen(self, target: int, nums) -> int:
    left = 0
    curr_sum = 0
    min_length = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0