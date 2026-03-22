class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rowLen = len(grid)
        colLen = len(grid[0])

        # we will run dfs starting from each cell, marking all connected cells as visited 
        # we will change them to 2

        # we will call dfs
        # if the cell as 1 ( If it has 2), its already taken care of. 
        # if its 0 , we can skip it.

        def _dfs(row=0, col=0):
            # Base case
            if row >= rowLen or col >= colLen or row < 0 or col < 0:
                return(0)
            
            if grid[row][col] == "1":
                grid[row][col] = "2"
                if row + 1 < rowLen:                
                    _dfs(row + 1, col) 
                if row -1  >= 0:
                    _dfs(row - 1, col)  
                if col +1  < colLen:
                    _dfs(row, col + 1)  
                if col -1 >= 0:
                    _dfs(row, col - 1)
                
                return(1)
            else:
                return(0)

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == "1":
                    count += _dfs(row, col)
        return(count)

        

