class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        創鄰接表
        """
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j)) # (cost, node)
                adj[j].append((dist, i))
        
        res = 0
        visited = set()
        min_h = [(0,0)]  # just a init point

        while len(visited) < n:
            cost, node = heapq.heappop(min_h)
            if node in visited:
                continue
            
            res += cost
            visited.add(node)

            for nei_cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_h, (nei_cost, nei))

        return res