class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited = set()
        graph = {}

        for i in range(n):
            graph[i] = []
        
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        def isCycle(child, parent):
            if child in visited:
                return True
            visited.add(child)

            for neighbor in graph[child]:
                if not neighbor == parent:
                    if isCycle(neighbor, child):
                        return True
            
        if isCycle(0, 0):
            return(False)
        
        return n == len(visited)

        


