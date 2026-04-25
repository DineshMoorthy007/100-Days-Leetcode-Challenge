class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = defaultdict(list)
                
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
                                        
        heap = [(passingFees[0], 0, 0)]
        best = dict()
                                                    
        while heap:
            cost, node, time = heapq.heappop(heap)
            
            if (node, time) in best and best[(node, time)] < cost:
                continue
                            
            if node == n - 1:
                return cost
                                                            
            for nei, t in graph[node]:
                new_time = time + t
                if new_time > maxTime:
                    continue
                
                new_cost = cost + passingFees[nei]
                
                if best.get((nei, new_time), float('inf')) > new_cost:
                    best[(nei, new_time)] = new_cost
                    heapq.heappush(heap, (new_cost, nei, new_time))
                                    
        return -1
