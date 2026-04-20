class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        1. Build adj list: for every pair (i, j) compute Manhattan Distance 
            and store as (cost, neighbor) in both directions
        2. Use a min heap to greadily pick the cheapest edge to an unvisited node
        3. Repeat until all node are included in the MST.
        """

        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        
        min_h = [(0,0)] # init point (cost=0, start from node 0)
        visited = set()
        res = 0 # accumulate total minimun cost

        while len(visited) < n:
            cost, node = heapq.heappop(min_h)
            if node in visited:
                continue
                
            visited.add(node)
            res += cost

            for nei_cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_h, (nei_cost, nei))
        
        return res
