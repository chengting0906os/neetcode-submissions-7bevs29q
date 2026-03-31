class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def search():
            q = deque()
            for r in range(rows):
                for c in range(cols):
                    if (r==0 or r==rows-1 or c==0 or c==cols-1) and board[r][c] == 'O':
                        q.append((r,c))
            
            while q:
                r, c = q.popleft()
                board[r][c] = 'T'
                for a, b in directions:
                    nr = r + a
                    nc = c + b
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] =='O':
                        q.append((nr, nc))
        search()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

