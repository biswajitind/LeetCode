class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

# 00 01 02 03 04 05 06 07 08
# 10 11 12 13 14 15 16
# 20 21 22 23 24
# 30 31 32 33 34 45
# 40
# 50
# 60
# 70
# 80


        cols = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        blocks = [set() for i in range(9)]

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == '.':
                    continue
                
                blockId = (col // 3) * 3 + (row // 3)
                if (val in rows[row] or
                    val in cols[col] or 
                    val in blocks[blockId]):
                    return(False)
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    blocks[blockId].add(board[row][col])
        return(True)

