"""
Given a string s, find the length of the longest 
substring
without repeating characters.

"""

def lengthOfLongestSubstring(self, s: str) -> int:
    unique = set()
    l,r,ans = 0,0,0
    while(r < len(s)):
        if s[r] not in unique:
            unique.add(s[r])
            r += 1
        else:
            unique.remove(s[l])
            l += 1
        ans = max(ans,r-l)
    return ans