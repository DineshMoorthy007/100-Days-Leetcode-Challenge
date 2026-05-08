class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = 10**18

        @lru_cache(None)
        def dfs(i, prev_color, neighborhoods):
            if neighborhoods < 0:
                return INF
            if i == m:
                return 0 if neighborhoods == 0 else INF

            if houses[i] != 0:
                new_neighborhoods = neighborhoods - (1 if houses[i] != prev_color else 0)
                return dfs(i + 1, houses[i], new_neighborhoods)

            ans = INF
            for color in range(1, n + 1):
                new_neighborhoods = neighborhoods - (1 if color != prev_color else 0)
                ans = min(
                    ans,
                    cost[i][color - 1] + dfs(i + 1, color, new_neighborhoods)
                )
            return ans

        res = dfs(0, 0, target)
        return -1 if res >= INF else res
