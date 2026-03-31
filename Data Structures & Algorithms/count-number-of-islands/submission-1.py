class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        q = deque()

        def dfs(row, col):
            if (row < 0 or col < 0 
                or row == rows or
                col == cols or grid[row][col] == "0"):
                return 

            q.append((row, col))
            grid[row][col] = "0"
            while q:
                r, c = q.popleft()
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
                    

        return res