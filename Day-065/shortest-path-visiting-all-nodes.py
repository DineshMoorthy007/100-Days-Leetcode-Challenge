class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1

        queue = deque()
        visited = set()

        for i in range(n):
            mask = (1 << i)
            queue.append((i, mask))
            visited.add((i, mask))

        steps = 0

        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()

                if mask == target_mask:
                    return steps

                for nei in graph[node]:
                    new_mask = mask | (1 << nei)

                    if (nei, new_mask) not in visited:
                        visited.add((nei, new_mask))
                        queue.append((nei, new_mask))

            steps += 1
