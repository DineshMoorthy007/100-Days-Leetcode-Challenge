class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
                                    
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
                                                    
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
                        
            for nei, w in graph[node]:
                if dist[nei] > d + w:
                    dist[nei] = d + w
                    heapq.heappush(heap, (dist[nei], nei))
        
        @lru_cache(None)
        def dfs(node):
            if node == n:
                return 1
            
            res = 0
            for nei, _ in graph[node]:
                if dist[nei] < dist[node]:
                    res += dfs(nei)
                
            return res % MOD
                        
        return dfs(1)
