class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        parents = defaultdict(list)
        level = {beginWord}
        found = False
        
        while level and not found:
            next_level = set()
            word_set -= level
            
            for word in level:
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = word[:i] + ch + word[i + 1:]
                        if nxt in word_set:
                            next_level.add(nxt)
                            parents[nxt].append(word)
                            if nxt == endWord:
                                found = True
            
            level = next_level
        
        res = []
        path = [endWord]
        
        def backtrack(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                backtrack(p)
                path.pop()
        
        if found:
            backtrack(endWord)
        
        return res
