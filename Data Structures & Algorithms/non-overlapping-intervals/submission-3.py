class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 依 start 排序
        intervals.sort(key=lambda x: x[0])

        prev_end = intervals[0][1]
        removed = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # 發生 overlap
            if start < prev_end:
                removed += 1
                # 保留 end 較小的那個（greedy 核心）
                prev_end = min(prev_end, end)
            else:
                # 沒重疊，直接更新為目前 interval
                prev_end = end

        return removed
