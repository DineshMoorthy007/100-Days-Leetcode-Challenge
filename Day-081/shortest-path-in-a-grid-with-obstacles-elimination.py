class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
            
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
                        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
                                
        while queue:
            r, c, rem, steps = queue.popleft()
                                                    
            if r == m - 1 and c == n - 1:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_rem = rem - grid[nr][nc]
                
                    if new_rem >= 0:
                        state = (nr, nc, new_rem)
                    
                        if state not in visited:
                            visited.add(state)
                            queue.append((nr, nc, new_rem, steps + 1))
                                                            
        return -1
