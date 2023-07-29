"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the 
following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""
import math
def getPermutation(self, n: int, k: int) -> str:
    nums = [i+1 for i in range(n)]
    return self.getPermutation2(k-1, nums)
def getPermutation2(self, k, nums) -> str:
    n = len(nums) 
    if n == 1: 
        return str(nums[0])
    if k == 0: return "".join([str(i) for i in nums])
    p_n_1 = math.factorial(n-1) 
    idx = k//p_n_1
    return str(nums[idx]) + self.getPermutation2(k%p_n_1, nums[:idx]+nums[idx+1:])
