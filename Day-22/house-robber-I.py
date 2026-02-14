class Solution(object):
    def rob(self, nums):
        prev2 = 0
        prev1 = 0 

        for n in nums:
            curr = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = curr

        return prev1
