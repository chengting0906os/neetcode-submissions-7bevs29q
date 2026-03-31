class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        days = 0
        bananas = 0

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    bananas += 1
        
        def add_x(r, c):
            nonlocal bananas
            if (r<0 or c<0 or r==rows or c==cols 
            or grid[r][c] == 2 or grid[r][c] == 0):
                return
            grid[r][c] = 2
            q.append((r,c))
            bananas -= 1

        while q and bananas > 0:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                add_x(r+1, c)
                add_x(r-1, c)
                add_x(r, c+1)
                add_x(r, c-1)
            days += 1
                


        return days if bananas == 0 else -1