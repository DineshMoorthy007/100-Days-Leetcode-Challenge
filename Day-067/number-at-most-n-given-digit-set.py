from functools import lru_cache
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(s)
               
        res = 0
        d = len(digits)
                               
        for i in range(1, m):
            res += d ** i

        @lru_cache(None)                                       
        def dfs(i, tight):
            if i == m:
                return 1
                                                                                   
            count = 0
            for digit in digits:
                if tight :
                    if digit > s[i]:
                        break
                    elif digit == s[i]:
                        count += dfs(i + 1, True)
                    else:
                        count += dfs(i + 1, False)
                else:
                    count += dfs(i + 1, False)
            
            return count
        
        return res + dfs(0, True)
