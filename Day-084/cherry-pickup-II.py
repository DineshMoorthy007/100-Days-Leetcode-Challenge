class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
            
        dp = [[[-float('inf')]*n for _ in range(n)] for _ in range(m)]
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]
                        
        for r in range(1, m):
            for c1 in range(n):
                for c2 in range(n):
                    max_val = -float('inf')
                    for d1 in [-1,0,1]:
                        for d2 in [-1,0,1]:
                            pc1, pc2 = c1-d1, c2-d2
                            if 0 <= pc1 < n and 0 <= pc2 < n:
                                max_val = max(max_val, dp[r-1][pc1][pc2])
                                                        
                    if max_val == -float('inf'):
                        continue
                                                        
                    dp[r][c1][c2] = max_val + grid[r][c1]
                            
                    if c1 != c2:
                        dp[r][c1][c2] += grid[r][c2]
                        
        return max(max(row) for row in dp[-1])
