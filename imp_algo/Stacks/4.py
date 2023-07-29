"""
rempving duplicate letters in a string and returning it in the smallest lexicographical order

"""
def removeDuplicateLetters(self, s: str) -> str:
    stack, cnt = [], {}
    for c in s:
        cnt[c] = 1 + cnt.get(c,0)
    for c in s:
        if c not in stack:
            while stack and c <= stack[-1] and cnt[stack[-1]] > 1:
                cnt[stack.pop()] -= 1
            stack.append(c)
        else:
            cnt[c] -= 1
    return "".join(stack) 