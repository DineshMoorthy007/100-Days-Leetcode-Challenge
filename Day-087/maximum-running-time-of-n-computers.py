class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n
            
        def canRun(time):
            total = 0
            for b in batteries:
                total += min(b, time)
            return total >= n * time
                                                        
        while left < right:
            mid = (left + right + 1) // 2
            if canRun(mid):
                left = mid
            else:
                right = mid - 1
                                        
        return left
