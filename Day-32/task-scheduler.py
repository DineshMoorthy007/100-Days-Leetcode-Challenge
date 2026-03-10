class Solution(object):
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            temp = []
…                heapq.heappush(heap, item)

            if heap:
                time += cycle

        return time
