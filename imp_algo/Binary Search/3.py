"""
Given an integer array nums, return an integer array counts where counts[i] 
is the number of smaller elements to the right of nums[i].
"""
from sortedcontainers import SortedList 
def countSmaller(self, nums) :
    sorted_list = SortedList([])
    result = []
    for i in range(len(nums)-1,-1,-1):
        result.append(sorted_list.bisect_left(nums[i]))
        sorted_list.add(nums[i])
    return result[::-1]
