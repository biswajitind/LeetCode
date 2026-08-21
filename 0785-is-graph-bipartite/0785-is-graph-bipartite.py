from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {
            -1: set(),
            1: set()
        }

        def dfs(node, key):
            if node in visited[key]:
                return(True)
            if node in visited[-1 * key]:
                return(False)
            
            visited[key].add(node)
            for n in graph[node]:
                if not dfs(n, -1 * key):
                    return(False)
            return(True)
        
        for x in range(len(graph)):
            visited = {
                -1: set(),
                1: set()
            }            
            if not dfs(x, 1):
                return(False)

        return(True)