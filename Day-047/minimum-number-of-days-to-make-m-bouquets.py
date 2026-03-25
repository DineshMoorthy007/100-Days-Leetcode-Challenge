class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        def can_make(days):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if can_make(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
