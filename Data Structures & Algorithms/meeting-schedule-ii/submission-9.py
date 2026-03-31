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
        # list.append (start, +1) (end,-1)
        room = []
        active = 0
        res = 0

        for i in intervals:
            room.append((i.start, 1))
            room.append((i.end, -1))

        room.sort()

        for r in room:
            active += r[1]
            res = max(res, active)
        
        return res
