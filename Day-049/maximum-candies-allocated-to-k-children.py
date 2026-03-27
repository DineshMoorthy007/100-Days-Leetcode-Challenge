class Solution(object):
    def maximumCandies(self, candies, k):
        def can_allocate(x):
            count = 0
            for c in candies:
                count += c // x
            return count >= k

        left, right = 1, max(candies)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if can_allocate(mid):
                answer = mid
                left = mid + 1   # maximize
            else:
                right = mid - 1

        return answer
