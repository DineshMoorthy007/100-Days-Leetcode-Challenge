def shipWithinDays(self, weights, days):
    l , r = max(weights) ,sum(weights)
    res = r

    def canDays(cap) :
        ships ,cur = 1 ,cap
        for w in weights :
            if cur - w < 0 :
                ships += 1
                cur = cap
            cur -= w
        return ships <= days

    while l <= r :
        cap = (l + r) // 2
        if canDays(cap) :
            res = min(res , cap)
            r = cap - 1
        else :
            l = cap + 1
    return res    
