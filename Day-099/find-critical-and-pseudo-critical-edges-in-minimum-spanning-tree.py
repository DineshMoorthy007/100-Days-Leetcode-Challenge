class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [e + [i] for i, e in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        
        def kruskal(force_edge=None, banned_edge=None):
            dsu = DSU(n)
            total = 0
            count = 0
            
            if force_edge is not None:
                u, v, w, idx = force_edge
                if dsu.union(u, v):
                    total += w
                    count += 1
            
            for u, v, w, idx in edges:
                if idx == banned_edge:
                    continue
                if force_edge is not None and idx == force_edge[3]:
                    continue
                if dsu.union(u, v):
                    total += w
                    count += 1
                    if count == n - 1:
                        break
            
            return total if count == n - 1 else float('inf')
        
        base = kruskal()
        critical, pseudo = [], []
        
        for edge in edges:
            idx = edge[3]
            without = kruskal(banned_edge=idx)
            
            if without > base:
                critical.append(idx)
            else:
                with_edge = kruskal(force_edge=edge)
                if with_edge == base:
                    pseudo.append(idx)
        
        return [critical, pseudo]
