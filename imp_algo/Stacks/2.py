"""
check if parenthesis are valid in O(n)

"""

def isValid(self, s: str) -> bool:
    opens = {'(','{','['}
    hmap = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for ch in s:
        if ch in hmap.keys() and len(stack) > 0 and hmap[ch] == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return True if len(stack) == 0 else False
