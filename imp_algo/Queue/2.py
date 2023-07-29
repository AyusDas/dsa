"""
maximum circular subarray sum

"""

def maxSubarraySumCircular(self, nums) -> int:
    minGlobal = minCurrent = nums[0]
    total = sum(nums)
    for i in nums[1:]:
        minCurrent = min(i,minCurrent+i)     
        if minCurrent < minGlobal:
            minGlobal = minCurrent
    maxGlobal = maxCurrent = nums[0]
    for i in nums[1:]:
        maxCurrent = max(i,maxCurrent+i)     
        if maxCurrent > maxGlobal:
            maxGlobal = maxCurrent
    return max(maxGlobal,total-minGlobal) if total != minGlobal else maxGlobal
