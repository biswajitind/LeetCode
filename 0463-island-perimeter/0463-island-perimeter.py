class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # simple no recursion solution

        peri = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    pass
                else:
                    landP = 4
                    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for r, c in directions:
                        row1, col1 = row+r, col+c
                        if row1 >= 0 and col1 >= 0 and row1 < len(grid) and col1 < len(grid[0]):
                            if grid[row1][col1] == 1:
                                landP -= 1
                    peri += landP
        return(peri)

