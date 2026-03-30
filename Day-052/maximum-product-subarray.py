class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmn,cmx = 1,1

        for n in nums :        
            t = cmx * n
            cmx = max(n * cmx, n * cmn, n)
            cmn = min(t, n * cmn, n)
            res = max(cmn,cmx,res)

        return res
