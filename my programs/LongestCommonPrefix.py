class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        s = strs[0]
        res = len(s)
        for i in range(1, n):
            s1 = strs[i]
            j = 0
            count = 0
            while j < len(s) and j < len(s1):
                if s[j] == s1[j]:
                    count += 1
                else:
                    break
                j += 1
            if res > count:
                res = count
        return strs[0][:res]
