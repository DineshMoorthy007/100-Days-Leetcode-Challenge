class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        window_sum = [0] * (n - k + 1)
        curr = sum(nums[:k])
        window_sum[0] = curr

        for i in range(1, n - k + 1):
            curr += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr

        left = [0] * len(window_sum)
        best = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best]:
                best = i
            left[i] = best

        right = [0] * len(window_sum)
        best = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best]:
                best = i
            right[i] = best

        result = [-1, -1, -1]
        max_total = 0
        for mid in range(k, len(window_sum) - k):
            l = left[mid - k]
            r = right[mid + k]

            total = window_sum[l] + window_sum[mid] + window_sum[r]

            if total > max_total:
                max_total = total
                result = [l, mid, r]

        return result
