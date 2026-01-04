def lengthOfLongestSubstring(self, s):
    Cset = set()
    l = 0
    r = 0
    for i in range(len(s)):
        while s[i] in Cset:
            Cset.remove(s[l])
            l += 1
        Cset.add(s[i])
        r = max(r, i - l + 1)
    return r
