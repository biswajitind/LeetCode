class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        size = len(grid)

        def cost(y, ext):
            r = 0
            center = size // 2

            for i in range(size):
                for j in range(size):
                    if (
                        (i == j and i <= center) 
                        or (i+j == size-1 and i <= center) 
                        or (i > center and j == center)
                    ):
                        if grid[i][j] != y:
                            r += 1
                    else:
                        if grid[i][j] != ext:
                            r += 1
            return(r)
        
        return(min(cost(0, 1), cost(0, 2), cost(1, 0), cost(1, 2), cost(2, 0), cost(2, 1)))