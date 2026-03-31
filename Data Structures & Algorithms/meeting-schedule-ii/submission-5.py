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
        mp = defaultdict(int)
        # [(0,40),(5,10),(15,20),(15,25)]
        for inter in intervals:
            mp[inter.start] += 1
            mp[inter.end] -= 1
        active = 0
        res = 0
        for i in sorted(mp.keys()):
            active += mp[i]
            res = max(res, active)
        return res