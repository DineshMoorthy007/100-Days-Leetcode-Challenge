class Solution(object):
    def maxValue(self, n, index, maxSum):
        def calc(mid):
            left_len = index
            right_len = n - index - 1

            def sum_side(length):
                if mid > length:
                    return (mid - 1 + mid - length) * length // 2
                else:
                    return (mid - 1 + 1) * (mid - 1) // 2 + (length - (mid - 1))

            return mid + sum_side(left_len) + sum_side(right_len)

        left, right = 1, maxSum
        answer = 1

        while left <= right:
            mid = (left + right) // 2

            if calc(mid) <= maxSum:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
