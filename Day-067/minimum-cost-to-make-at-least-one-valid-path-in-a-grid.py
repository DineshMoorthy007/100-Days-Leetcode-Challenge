class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
                
        dq = deque([(0, 0, 0)])
        visited = set()
                            
        while dq:
            cost, r, c = dq.popleft()
                                                
            if (r, c) in visited:
                continue
            visited.add((r, c))
                                                                                    
            if r == m - 1 and c == n - 1:
                return cost
                                                                                                                
            for i, (dr, dc) in enumerate(directions, 1):
                nr, nc = r + dr, c + dc
                                                                                                                                                
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[r][c] == i:
                        dq.appendleft((cost, nr, nc))
                    else:
                        dq.append((cost + 1, nr, nc))
