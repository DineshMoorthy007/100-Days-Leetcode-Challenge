class Solution(object):
    def maxDistance(self, position, m):
        position.sort()

        def can_place(dist):
            count = 1
            last = position[0]

            for pos in position:
                if pos - last >= dist:
                    count += 1
                    last = pos

            return count >= m

        left, right = 1, position[-1] - position[0]
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if can_place(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
