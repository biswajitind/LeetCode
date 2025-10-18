class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return(s)
            
        n = len(s)
        numCols = len(s)
        matrix = [[None for _ in range(numCols+1)] for _ in range(numRows+1)]
        

        # My intuition is to build a matrix, with fixed number of rows,
        # as grow in columns as ling as needed till we finish the Characters in the 
        # input string. 
        r, c = 0,0 
        rInc, cInc = 1,0
        for ch in s:
            
            matrix[r][c] = ch
            if r+rInc >= numRows:
                rInc = -1
                cInc = 1
            if r+rInc < 0:
                rInc = 1
                cInc = 0
            r += rInc
            c += cInc
        
        result = ''        
        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j]:
                    result = f'{result}{matrix[i][j]}'
        return(result)




        








        