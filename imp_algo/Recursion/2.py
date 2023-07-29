"""
Given a string expression of numbers and operators, return 
all possible results from computing all the different possible ways to 
group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit 
integer and the number of different results does not exceed 10^4.
"""
def diffWaysToCompute(self, expression: str):
    def calc(l,r,op):
        if op == '+':
            return l+r
        elif op == '-':
            return l-r
        elif op == '*':
            return l*r
    def recFunc(s):
        if s.isdigit():
            return [int(s)]
        res = []
        for i in range(len(s)):
            if s[i] in ['+','-','*']:
                leftRes = recFunc(s[:i])
                rightRes = recFunc(s[i+1:])
                for left in leftRes:
                    for right in rightRes:
                        res.append(calc(left, right, s[i]))
        return res
    return recFunc(expression)