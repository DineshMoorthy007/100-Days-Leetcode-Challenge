class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
            
        valid = []
        for row in seats:
            masks = []
            for mask in range(1 << n):
                ok = True
                for j in range(n):
                    if (mask & (1 << j)):
                        if row[j] == '#':
                            ok = False
                        if j > 0 and (mask & (1 << (j - 1))):
                            ok = False
                if ok:
                    masks.append(mask)
            valid.append(masks)
                                                        
        dp = [{} for _ in range(m)]
        
        for mask in valid[0]:
            dp[0][mask] = bin(mask).count('1')
    
        for i in range(1, m):
            for mask in valid[i]:
                for pmask in dp[i - 1]:
                    if (mask & (pmask << 1)) == 0 and (mask & (pmask >> 1)) == 0:
                        dp[i][mask] = max(
                            dp[i].get(mask, 0),
                            dp[i - 1][pmask] + bin(mask).count('1')
                        )
        
        return max(dp[-1].values(), default=0)
