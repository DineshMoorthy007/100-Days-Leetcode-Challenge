class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for s,e in intervals[1:] :
            if s >= prevEnd:
                prevEnd = e
            else :
                res += 1
                prevEnd = min(e,prevEnd)

        return res
