class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        n = len(intervals)
        i = 1

        while i < n:
            if res[-1][1] >= intervals[i][0]:
                temp = [0,0]
                temp[0] = min(res[-1][0],intervals[i][0])
                temp[1] = max(res[-1][1],intervals[i][1])
                res[-1] = temp
            else:
                res.append(intervals[i])
            i+=1
        return res
