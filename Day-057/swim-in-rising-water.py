class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minH = [[grid[0][0],0,0]]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        visit.add((0,0))
        while minH :
            t, r, c = heapq.heappop(minH)
            visit.add((r,c))

            if r == n - 1 and c == n - 1:
                return t

            for dr,dc in directions :
                nr,nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr == n or nc == n
                    or (nr,nc) in visit):
                    continue
                visit.add((nr,nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
