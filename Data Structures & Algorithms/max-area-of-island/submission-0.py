class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            count = 1

            while q:
                r, c = q.popleft()
                for a, b in directions:
                    nr = r + a
                    nc = c + b
                    if nr < 0 or nr == rows or nc == cols or 0 > nc or grid[nr][nc] ==0:
                        continue
                    grid[nr][nc] = 0
                    count += 1
                    q.append((nr,nc))
            
            
            return count
        
        



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r,c))

        return res

            
