class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Build adj list (cost)
        min_heap to count cost
        """
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1 - y2)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        
        min_heap = [(0, 0)]
        visited = set()
        res = 0

        while min_heap:
            cost, idx = heapq.heappop(min_heap)
            if idx in visited:
                continue
            
            visited.add(idx)
            res += cost
            for nei_cost, nei in adj[idx]:
               heapq.heappush(min_heap,(nei_cost, nei))
        
        return res