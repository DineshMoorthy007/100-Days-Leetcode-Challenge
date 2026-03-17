class Solution(object):
    def isHappy(self, n):
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = fast = n
        
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
