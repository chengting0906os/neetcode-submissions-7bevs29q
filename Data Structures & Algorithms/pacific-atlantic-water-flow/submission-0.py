class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pac = [[False for _ in range(cols)] for _ in range(rows)]
        atl = [[False for _ in range(cols)] for _ in range(rows)]
        res = []
        

        def bfs(pos_list, ocean):
            q = deque(pos_list)
            
            while q:
                cur = q.popleft()
                r, c = cur[0], cur[1]
                ocean[r][c] = True
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if rows > nr >= 0 and cols > nc >= 0 and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
                        q.append((nr, nc))
        
        pacific = []
        atlantic = []

        for i in range(rows):
            pacific.append((i, 0))
            atlantic.append((i, cols-1))  
        
        for i in range(cols):
            pacific.append((0, i))
            atlantic.append((rows-1, i))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)
        
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        
        return res
