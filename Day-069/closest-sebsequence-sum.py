class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
            
        def subset_sums(arr):
            res = [0]
            for num in arr:
                res += [num + x for x in res]
            return res
                                                        
        left = subset_sums(nums[:n//2])
        right = subset_sums(nums[n//2:])
                                                                    
        right.sort()
        res = float('inf')
        
        for s in left:
            remain = goal - s
            idx = bisect_left(right, remain)
            
            if idx < len(right):
                res = min(res, abs(s + right[idx] - goal))
            if idx > 0:
                res = min(res, abs(s + right[idx-1] - goal))
        
        return res
