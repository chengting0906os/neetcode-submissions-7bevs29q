class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 記錄最遠的 start
        max_val = max(start for start, _ in intervals)
        mp = [0] * (max_val+1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])
        
        res = []
        farthest_end = -1
        start = None
        for i in range(len(mp)):
            if mp[i] != 0:
                if start is None:
                    start = i
                
                farthest_end = max(mp[i]-1, farthest_end)
            if farthest_end == i:
                res.append([start, farthest_end])
                farthest_end = -1
                start = None

        if start is not None:
            res.append([start, farthest_end])

        return res
