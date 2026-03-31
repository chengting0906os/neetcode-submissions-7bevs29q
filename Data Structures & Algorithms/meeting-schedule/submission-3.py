"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)
        
        pre_end = intervals[0].end
        for i in range(1, len(intervals)):
            if pre_end > intervals[i].start:
                return False
            pre_end = intervals[i].end
        
        return True