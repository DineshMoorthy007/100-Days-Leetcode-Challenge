class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    subs = backtrack(end)
                    for sub in subs:
                        result.append(word + (" " + sub if sub else ""))

            memo[start] = result
            return result

        return backtrack(0)
