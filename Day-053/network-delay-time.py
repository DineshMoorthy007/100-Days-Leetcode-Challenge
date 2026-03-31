class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))

        mHeap = [(0,k)]
        visit = set()
        t = 0
        while mHeap:
            w1, n1 = heapq.heappop(mHeap)
            if n1 in visit :
                continue
            visit.add(n1)
            t = max(t,w1)

            for n2, w2 in edges[n1] :
                if n2 not in visit :
                    heapq.heappush(mHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1
