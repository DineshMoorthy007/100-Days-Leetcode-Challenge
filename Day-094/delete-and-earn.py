class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
                
        for num in nums:
            points[num] = points.get(num, 0) + num
                                            
        max_num = max(nums)
        take, skip = 0, 0
                                                                    
        for i in range(max_num + 1):
            take_i = skip + points.get(i, 0)
            skip_i = max(skip, take)
            take, skip = take_i, skip_i
                                            
        return max(take, skip)
