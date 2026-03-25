class Solution(object):
    def splitArray(self, nums, k):
        def can_split(max_sum):
            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > max_sum:
                    subarrays += 1
                    curr_sum = 0
                curr_sum += num

            return subarrays <= k

        left, right = max(nums), sum(nums)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if can_split(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
