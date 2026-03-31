class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))
        
        min_heap = [(0, k)]
        t = 0
        visited = set()

        while min_heap:
            t1, v1 = heapq.heappop(min_heap)
            if v1 in visited:
                continue
            t = t1
            visited.add(v1)

            for t2, v2 in adj[v1]:
                heapq.heappush(min_heap, (t1+t2, v2))
        
        return t if len(visited) == n else -1
