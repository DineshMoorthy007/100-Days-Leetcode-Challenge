class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        dp = nums[:]
                
        for i in range(len(nums)):
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])
                                                
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
                
            if dp[i] > 0:
                dq.append(i)
                                    
            if dq and i - dq[0] >= k:
                dq.popleft()
                                                        
        return max(dp)
