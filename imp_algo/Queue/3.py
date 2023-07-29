"""
Given an array of integers nums and an integer limit, return the size of 
the longest non-empty subarray such that the absolute difference 
between any two elements of this subarray is less than or equal to limit.

"""
import collections
def longestSubarray(self, nums, limit: int):
    maxDeck = collections.deque()
    minDeck = collections.deque()
    start = 0
    for end in nums:
        while len(maxDeck) and end > maxDeck[-1] : maxDeck.pop()
        while len(minDeck) and end < minDeck[-1] : minDeck.pop()
        maxDeck.append(end)
        minDeck.append(end)
        if maxDeck[0] - minDeck[0] > limit:
            if maxDeck[0] == nums[start] : maxDeck.popleft()
            if minDeck[0] == nums[start] : minDeck.popleft()
            start += 1
    return len(nums)-start