class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(diff):
            best = curr = 0
                
            for x in diff:
                curr = max(x, curr + x)
                best = max(best, curr)
                                                        
            return best
                                                                    
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        gain1 = kadane([b - a for a, b in zip(nums1, nums2)])
        gain2 = kadane([a - b for a, b in zip(nums1, nums2)])
                    
        return max(sum1 + gain1, sum2 + gain2)
