def searchInsert(self, nums, target):
    l , r = 0 , len(nums) - 1

    while l <= r :
        m = (l + r) // 2

        if target == nums[m] :
            return m

        if target < nums[m] :
            r = m - 1

        if target > nums[m] :
            l = m + 1

    return l
