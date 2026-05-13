class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        route = []
        
        def dfs(node):
            
            while graph[node]:
                nxt = heapq.heappop(graph[node])
                dfs(nxt)
            
            route.append(node)
        
        dfs("JFK")
        
        return route[::-1]
