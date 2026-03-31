class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        squares_dict = defaultdict(set)

        for r in range(9):
            for c in range(9):
                now_num = board[r][c]
                if now_num == '.':
                    continue
                if now_num in rows_dict[r]:
                    return False
                if now_num in cols_dict[c]:
                    return False
                if now_num in squares_dict[(r//3, c//3)]:
                    return False
                
                rows_dict[r].add(now_num)
                cols_dict[c].add(now_num)
                squares_dict[(r//3, c//3)].add(now_num)    

        return True