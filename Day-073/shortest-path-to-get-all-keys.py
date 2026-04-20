class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = 0
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    keys = max(keys, ord(grid[i][j]) - ord('a') + 1)
                
        target = (1 << keys) - 1
                        
        queue = deque([(start[0], start[1], 0, 0)])
        visited = set([(start[0], start[1], 0)])
                                    
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
                                            
        while queue:
            r, c, mask, steps = queue.popleft()
            
            if mask == target:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                                                        
                if 0 <= nr < m and 0 <= nc < n:
                    cell = grid[nr][nc]
                
                    if cell == '#':
                        continue
    
                    new_mask = mask
                    if cell.islower():
                        new_mask |= (1 << (ord(cell) - ord('a')))
                    
                    if cell.isupper():
                        if not (mask & (1 << (ord(cell) - ord('A')))):
                            continue
                    
                    state = (nr, nc, new_mask)
                    
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, new_mask, steps + 1))

        return -1
