class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dfs(x):
            if x <= 1:
                return x
                                        
            return 1 + min(
                x % 2 + dfs(x // 2),
                x % 3 + dfs(x // 3)
            )
            
        return dfs(n)
