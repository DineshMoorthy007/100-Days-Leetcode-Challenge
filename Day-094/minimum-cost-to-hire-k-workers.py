class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        for q, w in zip(quality, wage):
            ratio = w / q
            workers.append((ratio, q))
                                                
        workers.sort()
                                                                
        heap = []
        total_quality = 0
        res = float('inf')
        
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_quality += q
            
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
                                        
            if len(heap) == k:
                res = min(res, total_quality * ratio)

        return res
