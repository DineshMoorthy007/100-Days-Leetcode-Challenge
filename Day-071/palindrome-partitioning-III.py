class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
            
        cost = [[0]*n for _ in range(n)]
                        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
                                                                
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0
                                                                            
        for i in range(1, n+1):
            for p in range(1, k+1):
                for j in range(i):
                    dp[i][p] = min(dp[i][p], dp[j][p-1] + cost[j][i-1])
                                                
        return dp[n][k]
