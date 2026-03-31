class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        steps = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for pr, pc in steps:
                        nr = r + pr
                        nc = c + pc
                        if not 0 <= nr < rows or not 0 <= nc < cols or grid[nr][nc] != 1:
                            res += 1
        return res
                        
                    
        
       
