"""
finding the longest increasing subsequence ending in the each position of the
input array when traversing it from left to right
time : O(nlogn)
"""
from bisect import bisect_right
def func(obstacles):
        stack,ans=[],[]
        for i in obstacles:
            br=bisect_right(stack,i) # for it be strictly increasing use bisect_left
            if br==len(stack):
                stack.append(i)
            else:
                stack[br]=i
            ans.append(br+1)
            
        return ans
