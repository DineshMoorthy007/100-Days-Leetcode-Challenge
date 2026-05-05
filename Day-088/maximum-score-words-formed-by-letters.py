class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = Counter(letters)
        n = len(words)
                
        word_counts = []
        word_scores = []
                            
        for word in words:
            cnt = Counter(word)
            word_counts.append(cnt)
            word_scores.append(sum(score[ord(c)-97] for c in word))
                                                            
        def backtrack(i, available):
            if i == n:
                return 0
                        
            res = backtrack(i+1, available)
                                                                                                            
            can_take = True
            for c in word_counts[i]:
                if word_counts[i][c] > available[c]:
                    can_take = False
                    break
                                
            if can_take:
                for c in word_counts[i]:
                    available[c] -= word_counts[i][c]
                
                res = max(res, word_scores[i] + backtrack(i+1, available))
                                
                for c in word_counts[i]:
                    available[c] += word_counts[i][c]
                        
            return res

        return backtrack(0, letter_count)
