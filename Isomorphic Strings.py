"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
def is_isomorphic(s,t):
    d = {}
    d.update({s[0]:t[0]})
    for i in range(1,len(s)):
        if s[i] not in d.keys():
            if t[i] in d.values():
                return False
            d.update({s[i]:t[i]})
        else:
            if d[s[i]]!=t[i]:
                return False
        a=d.keys()
    return True
print(is_isomorphic(s = "badc", t = "baba"))