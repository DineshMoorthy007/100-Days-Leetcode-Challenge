class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
                 
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
                                             
        right = 1
        res = left[-1]
                                                         
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            res += max(left[i], right)
                                     
        return res
