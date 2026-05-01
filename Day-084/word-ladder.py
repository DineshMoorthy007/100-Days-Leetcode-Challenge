class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
                        
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        step = 1
                                            
        while beginSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            next_set = set()
            
            for word in beginSet:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                                    
                        if new_word in endSet:
                            return step + 1
                        
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            next_set.add(new_word)
            
            beginSet = next_set
            step += 1
                            
        return 0
