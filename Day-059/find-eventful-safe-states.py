class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n

        for i in range(n):
            for nei in graph[i]:
                reverse_graph[nei].append(i)
            outdegree[i] = len(graph[i])

        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True

            for prev in reverse_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    queue.append(prev)

        return [i for i in range(n) if safe[i]]
