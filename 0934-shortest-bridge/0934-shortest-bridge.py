class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0, 1], [0, -1], [1, 0],[-1,0]]
        visited = set()

        def invalid(r, c):
            return(r < 0 or c < 0 or r >= len(grid) or c >= len(grid))

        # Place all the co-ordinates of 1 in the first island into a queue. 
        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r,c) in visited):
                return()
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # uses the visited set to work on. 
        def bfs():
            res, q = 0, deque(visited)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visited:
                            continue
                        if grid[curR][curC]:
                            return(res)
                        q.append([curR, curC])
                        visited.add((curR, curC))
                res += 1

        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    dfs(i, j)
                    return(bfs())
        


        




        

    


