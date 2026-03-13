def searchRange(self, nums, target):
        ls = self.bS(nums, target, True)
        rs = self.bS(nums, target, False)
        return [ls,rs]

def bS(self, nums , target , left) :
    l , r = 0 , len(nums) - 1
    i = -1

    while l <= r :
        mid = (l + r) // 2
        if target > nums[mid] :
            l = mid + 1

        elif target < nums[mid] :
            r = mid - 1
            
        else :
            i = mid
            if left :
                r = mid - 1
            else :
                l = mid + 1

    return i 
