class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Step 1: redefine the problem statement.
        # we know that 
        # - if we place a queen in a row (any position), we can not place any other queen in that row.
        # - since we have n rows and n queens, each queen must be placed in different rows.
        # - Thus the updated/simplified problem statement is
        # place n queen in n rows. This reduces the focus. we are no longer thinking of the entire board
        # for placement, but only a single row.
        # The high level ( the outer loop ) is now simply n iterations. Of-course we will have 
        # back tracking and also check each valid position in that row, however the problem
        # statement now seems simpler.
        board = [["."] * n for i in range(n)]
        counter = 7
        result = []

        def _safe(board, row, col):
            for r in range(n):
                if board[r][col] == 'Q':
                    return(False)
            for c in range(n):
                if board[row][c] == 'Q':
                    return(False)
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return(False)
                r -= 1
                c -= 1
            r, c = row, col
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return(False)
                r -= 1
                c += 1
            return(True)

        def _backtrack(board, row):

            for col in range (n):
                if _safe(board, row, col):
                    # if we are ble to place the last one. Its a success.
                    # push the board to result                        
                    board[row][col] = 'Q'
                    if row == n - 1:
                        copy = ["".join(row) for row in board]
                        result.append(copy)

                    _backtrack(board, row + 1)
                    board[row][col] = '.'
            return(False)


        _backtrack(board, 0)
        return(result)

        