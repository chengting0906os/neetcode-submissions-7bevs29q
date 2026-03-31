class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort
        intervals.sort(key=lambda x: x[0])
        pre_end = intervals[0][1]
        res = 0

        # [[1,2],[1,4],[2,5]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < pre_end:
                res += 1
                pre_end = min(pre_end, end)
            else:
                pre_end = end
        
        return res