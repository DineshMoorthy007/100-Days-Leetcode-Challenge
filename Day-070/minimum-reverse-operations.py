class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned_set = set(banned)
        res = [-1] * n
        
        parent = list(range(n + 2))
                
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
                                                                        
        def remove(x):
            parent[x] = find(x + 2)

        for b in banned:
            remove(b)
                            
        remove(p)
                                                        
        queue = deque([p])
        res[p] = 0
                                                                    
        while queue:
            i = queue.popleft()
                    
            left = max(0, i - k + 1)
            right = min(i, n - k)
                             
            L = 2 * left + k - 1 - i
            R = 2 * right + k - 1 - i

            if k % 2 == 0:
                L += (L % 2 == i % 2)
            else:
                L += (L % 2 != i % 2)

            j = find(L)
            
            while j <= R:
                res[j] = res[i] + 1
                queue.append(j)
                remove(j)
                j = find(j)

        return res
