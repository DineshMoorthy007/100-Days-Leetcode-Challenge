class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
            
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
                                    
        count = [1] * n
        ans = [0] * n
                                                
        def dfs(node, parent):
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node)
                    count[node] += count[nei]
                    ans[node] += ans[nei] + count[nei]
                                                
        def reroot(node, parent):
            for nei in graph[node]:
                if nei != parent:
                    ans[nei] = ans[node] - count[nei] + (n - count[nei])
                    reroot(nei, node)
                                    
        dfs(0, -1)
        reroot(0, -1)
                                                
        return ans
