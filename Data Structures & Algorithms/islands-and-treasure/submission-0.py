class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set()
        
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append(((r,c), 0)) 

        while q:
            cur = q.popleft()
            r, c = cur[0]
            step = cur[1]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if rows > nr >= 0 and cols > nc >= 0 and (nr,nc) not in seen and grid[nr][nc] == INF:
                    grid[nr][nc] = step + 1
                    q.append(((nr,nc), step+1))
                    seen.add((nr,nc))
