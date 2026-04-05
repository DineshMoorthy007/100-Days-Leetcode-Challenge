class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                parent[rootA] = rootB

        for a, b in connections:
            union(a, b)

        components = len(set(find(i) for i in range(n)))
        return components - 1
