class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ends = [job[1] for job in jobs]
        n = len(jobs)
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            
            j = bisect_right(ends, s, 0, i - 1)
            dp[i] = max(dp[i - 1], dp[j] + p)
        
        return dp[n]
