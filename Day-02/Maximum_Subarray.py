def maxSubArray(self, nums):
    sub = nums[0]
    cur = 0

    for n in nums :
        if cur < 0 :
            cur = 0
        cur += n
        sub = max(cur,sub)
    return sub
        
# for n in nums :
#     cur = max (n,cur + n)
#     sub = max (sub,cur)
# return sub
