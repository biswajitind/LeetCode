class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        self.islands = {}

        for i in range(m):
            for j in range(n):
                print(grid[i][j], '  ', end='')
            print()



        # This simply mark all neigbours as 0 if they are 1
        def _dfs(i, j, i_offset, j_offset):

            if i < 0 or i >= m or j < 0 or j >= n:
                return()

            if grid[i][j] == 0:
                return()

            grid[i][j] = 0
            key = str(i_offset) + '_' + str(j_offset)
            if key not in self.islands:
                self.islands[key] = []
            self.islands[key].append(str(i - i_offset) + str(j - j_offset))
                        
            for k, l in [[i+1, j], [i-1, j],[i, j+1], [i, j-1]]:
                if k >=0 and k < m and l >=0 and l < n:
                    if grid[k][l] == 1:
                        _dfs(k,l, i_offset, j_offset)
            return()

        for I in range(m):
            for J in range(n):
                if grid[I][J] == 1:
                    _dfs(I, J, I, J)
        
        values = self.islands.values()
        tmp = set()
        for v in values:
            tmp.add(''.join(v))

        print(self.islands)
        print(tmp)
        return(len(list(tmp)))