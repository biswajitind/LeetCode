class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0 

        ROW, COL = len(grid), len(grid[0])

        # populate the q with rotten oranges, and count the number of fresh one.
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if ( row < 0 or row >= ROW or
                         col < 0 or col >= COL  or
                         grid[row][col] != 1):
                         continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        if fresh:
            return(-1)
        else:
            return(time)
        







