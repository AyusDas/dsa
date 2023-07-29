"""
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
"""
def removeKdigits(self, nums: str, k: int) -> str:
    stack = []
    i = 0
    while i < len(nums):
        if len(stack) == 0:
            stack.append(nums[i])
            i += 1
            continue
        while len(stack) != 0 and k > 0:
            if stack[-1] > nums[i]:
                stack.pop()
                k -= 1
            else : break
        stack.append(nums[i])
        i += 1
    while k > 0:
        stack.pop()
        k -= 1
    i = 0
    res = "".join(stack) 
    while i < len(res) and res[i] == '0':
        i += 1
    res = res[i:]
    if res == "" : return "0"
    return res
