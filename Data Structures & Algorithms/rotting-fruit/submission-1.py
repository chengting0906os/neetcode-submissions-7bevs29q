class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        fresh = 0
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for pr, pc in steps:
                    nr = r + pr
                    nc = c + pc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            res += 1

        return res if fresh == 0 else -1