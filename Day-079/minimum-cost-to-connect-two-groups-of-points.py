class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
            
        min_cost = [min(cost[i][j] for i in range(m)) for j in range(n)]
                    
        @lru_cache(None)
        def dp(i, mask):
            if i == m:
                res = 0
                for j in range(n):
                    if not (mask & (1 << j)):
                        res += min_cost[j]
                return res
                                    
            res = float('inf')
            for j in range(n):
                res = min(
                    res,
                    cost[i][j] + dp(i + 1, mask | (1 << j))
                )
            
            return res
            
        return dp(0, 0)
