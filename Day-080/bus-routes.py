class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
                        
        stop_to_routes = defaultdict(list)
                                
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
                                                            
        visited_routes = set()
        visited_stops = set([source])
    
    queue = deque([(source, 0)])
    
    while queue:
        stop, buses = queue.popleft()
        
        for route in stop_to_routes[stop]:
            if route in visited_routes:
                continue
            
            visited_routes.add(route)
            
            for next_stop in routes[route]:
                if next_stop == target:
                    return buses + 1
                
                if next_stop not in visited_stops:
                    visited_stops.add(next_stop)
                    queue.append((next_stop, buses + 1))
    
    return -1
