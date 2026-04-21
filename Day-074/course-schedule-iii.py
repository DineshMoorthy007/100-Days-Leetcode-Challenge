class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
            
        total = 0
        heap = []
                        
        for duration, last_day in courses:
            total += duration
            heapq.heappush(heap, -duration)
                                                    
            if total > last_day:
                total += heapq.heappop(heap)
    
        return len(heap)
