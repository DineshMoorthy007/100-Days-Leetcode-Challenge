class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def compute(div):
            total = 0
            for num in nums:
                total += (num + div - 1) // div
            return total

        left, right = 1, max(nums)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if compute(mid) <= threshold:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
