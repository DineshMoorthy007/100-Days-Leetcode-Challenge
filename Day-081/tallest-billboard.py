class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
            
        for rod in rods:
            curr = dp.copy()
            for diff, height in curr.items():
                dp[diff + rod] = max(dp.get(diff + rod, 0), height)
                                                        
                new_diff = abs(diff - rod)
                dp[new_diff] = max(
                    dp.get(new_diff, 0),
                    height + min(diff, rod)
                )
                                                                
        return dp[0]
