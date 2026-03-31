"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#  [(0,40),(0,15),(5,10),(15,20)]
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for inter in intervals:

            if min_heap and min_heap[0] <= inter.start:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, inter.end)

        
        return len(min_heap)