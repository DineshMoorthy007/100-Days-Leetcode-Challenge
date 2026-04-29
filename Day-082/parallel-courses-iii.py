class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0]*(n+1)
                
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
                                        
        queue = deque()
        dp = [0]*(n+1)
                                                    
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i-1]
                    
        while queue:
            node = queue.popleft()
            
            for nei in graph[node]:
                dp[nei] = max(dp[nei], dp[node] + time[nei-1])
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                                        
        return max(dp)
