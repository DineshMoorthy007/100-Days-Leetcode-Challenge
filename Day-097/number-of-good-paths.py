class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return

            if size[px] < size[py]:
                px, py = py, px

            parent[py] = px
            size[px] += size[py]

        value_to_nodes = defaultdict(list)

        for i, v in enumerate(vals):
            value_to_nodes[v].append(i)

        result = n

        for value in sorted(value_to_nodes):

            for node in value_to_nodes[value]:
                for nei in graph[node]:
                    if vals[nei] <= value:
                        union(node, nei)

            count = defaultdict(int)

            for node in value_to_nodes[value]:
                root = find(node)
                count[root] += 1

            for c in count.values():
                result += c * (c - 1) // 2

        return result
