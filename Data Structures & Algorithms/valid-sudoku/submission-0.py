class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            vals = []
            for v in row:
                if v !='.':
                    vals.append(v)
            if len(vals) != len(set(vals)):
                return False
        for j in range(9):
            vals = []
            for i in range(len(board)):
                if board[i][j] != '.':
                    vals.append(board[i][j])
            if len(vals) != len(set(vals)):
                return False
        for box_row in range(3):
            for box_col in range(3):
                vals = []
                for r in range(3):
                    for c in range(3):
                        row_idx = box_row * 3 + r
                        col_idx = box_col * 3 + c
                        if board[row_idx][col_idx] != '.':
                            vals.append(board[row_idx][col_idx])
                if len(vals) != len(set(vals)):
                    return False
        return True


    