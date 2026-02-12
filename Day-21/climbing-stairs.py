class Solution(object):
    def climbStairs(self, n):
        a, b = 1,1
        for i in range (n -1) :
            a, b = (a + b),a

        return a
