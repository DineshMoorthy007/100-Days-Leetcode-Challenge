class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        n = len(parent)
                
        for i in range(1, n):
            tree[parent[i]].append(i)
                                
        res = 1
                                        
        def dfs(node):
            nonlocal res
            longest, second = 0, 0
                                                                    
            for child in tree[node]:
                length = dfs(child)
                
                if s[child] == s[node]:
                    continue

                if length > longest:
                    second = longest
                    longest = length
                elif length > second:
                    second = length

            res = max(res, longest + second + 1)
            return longest + 1
                
        dfs(0)
        return res
