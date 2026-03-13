def __init__(self, nums):
    self.pr = []
    cur = 0
    for n in nums :
        cur += n
        self.pr.append(cur)
        

def sumRange(self, left, right):
    if left > 0:
        r = self.pr[right] - self.pr[left - 1]
    else :
        r = self.pr[right]
    return r

##        rSum = self.pr[right]
##
##        lSum = self.pr[left-1] if left > 0 else 0
##
##        return rSum - lSum
