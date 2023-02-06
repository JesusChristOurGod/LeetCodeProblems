def canConstruct(ransomNote, magazine):
    freq = dict()
    for i in magazine:
        if i in freq.keys():
            freq.update({i:freq[i]+1})
        else:
            freq.update({i:1})
    for i in ransomNote:
        if not(i in freq.keys() and ransomNote.count(i)<=freq[i]):
            return False
    return True
print(canConstruct("aa","aab"))