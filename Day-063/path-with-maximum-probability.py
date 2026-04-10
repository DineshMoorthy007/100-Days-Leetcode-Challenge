class Solution:
        def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
            graph = defaultdict(list)

            for (u, v), prob in zip(edges, succProb):
                graph[u].append((v, prob))
                graph[v].append((u, prob))

            heap = [(-1.0, start_node)]
            visited = set()

            while heap:
                prob, node = heapq.heappop(heap)
                prob = -prob

                if node == end_node:
                    return prob

                if node in visited:
                    continue
                visited.add(node)
                
                for nei, p in graph[node]:
                    if nei not in visited:
                        heapq.heappush(heap, (-(prob * p), nei))

            return 0
