"""
Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.
"""

def findAnagrams(self, s: str, p: str) :
    l=0
    ans, pw, sw = [], {}, {}
    for r in range(26):
        sw[r] = 0
        pw[r] = 0
    for c in p:
        pw[ord(c)-ord('a')] += 1
    for r in range(0,len(s)+1):
        if sw == pw:
            ans.append(l)
        if r >= len(p) :
            sw[ord(s[l])-ord('a')] -= 1
            l += 1
        if r < len(s):    
            sw[ord(s[r])-ord('a')] += 1
    return ans