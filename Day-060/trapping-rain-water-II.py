class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        minhp = []
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1] :
                    heappush(minhp, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        
        res = 0
        mh = -1

        while minhp:
            h, r, c = heappop(minhp)
            mh = max(mh, h)
            res += mh - h

            n = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr, nc in n:
                if (nr < 0 or nc < 0 or nr == rows or nc == cols or
                    heightMap[nr][nc] == -1):
                    continue
                heappush(minhp, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        return res
