class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        p_count = Counter(p)
        window = Counter()

        for i in range(len(s)):
            window[s[i]] += 1

            if i >= len(p):
                if window[s[i - len(p)]] == 1:
                    del window[s[i - len(p)]]
                else:
                    window[s[i - len(p)]] -= 1

            if window == p_count:
                res.append(i - len(p) + 1)

        return res
