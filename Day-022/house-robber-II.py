class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev2 = prev1 = 0
            for n in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + n)
            return prev1            
    
        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )
