"""
Given an array of integers nums sorted in non-decreasing order, find the 
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

"""
from bisect import bisect_left, bisect_right
def searchRange(self, nums, target: int):
    def binary_search(arr, x):
        idx = bisect_left(arr,x)
        if idx != len(arr) and arr[idx] == x:
            return True
        else:
            return False
    if binary_search(nums,target) :
        start = bisect_left(nums,target)
        end = bisect_right(nums,target)
        return [start,end-1]
    else: return [-1,-1]
