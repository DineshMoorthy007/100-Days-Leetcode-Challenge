class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if not queue or len(queue) == n * n:
            return -1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        distance = -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

            distance += 1

        return distance
