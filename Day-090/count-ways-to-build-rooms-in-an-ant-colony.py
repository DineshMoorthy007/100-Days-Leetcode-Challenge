class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        tree = [[] for _ in range(n)]
                
        for i in range(1, n):
            tree[prevRoom[i]].append(i)
                                
        fact = [1] * (n + 1)
        invfact = [1] * (n + 1)
                                            
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
                                                            
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD
        
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD
                                            
        def dfs(node):
            size = 1
            ways = 1
            for child in tree[node]:
                child_size, child_ways = dfs(child)
                ways = ways * child_ways % MOD
                ways = ways * comb(size - 1 + child_size, child_size) % MOD
                size += child_size
                                                                
            return size, ways
        
        return dfs(0)[1]
