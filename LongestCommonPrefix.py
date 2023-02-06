class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ind = 0
        min_len = 100000
        res=""
        for i, s in enumerate(strs):
            if len(s)<min_len:
                ind = i
                min_len=len(s)
        key = strs[ind]
        for i, s in enumerate(key):
            if any([x[i]!=s for x in strs]):
                # strs = list(map(lambda s: s[:-1] if len(s)>1 else s, strs))
                break
            res+=s
        return res


a = Solution()
strs = ["flower", "flow", "flight"]
print(a.longestCommonPrefix(strs))
print([s != strs[0] for s in strs])