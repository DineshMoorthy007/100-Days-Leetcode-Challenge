class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)
                
        freq = [[0]*26 for _ in range(m)]
        
        for word in words:
            for i, ch in enumerate(word):
                freq[i][ord(ch)-97] += 11
                                                    
        dp = [0]*(n+1)
        dp[0] = 1
                                                                
        for i in range(m):
            for j in range(n-1, -1, -1):
                c = ord(target[j]) - 97
                dp[j+1] += dp[j] * freq[i][c]
                dp[j+1] %= MOD
                                            
        return dp[n]
