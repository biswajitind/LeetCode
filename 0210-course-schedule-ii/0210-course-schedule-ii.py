class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        output = []        # Final output
        selected = set()   # added to output. using this for quick check in O(1) time.
        visited = set()    # for detecting cycle in the recursion loop. 

        adjList = {node: [] for node in range(numCourses)}
        for crs, dep in prerequisites:
            adjList[crs].append(dep)


        def _dfs(crs):
            if crs in selected:
                return(True)
            if crs in visited:
                return(False)
            

            
            visited.add(crs)
            for dep in adjList[crs]:
                if not _dfs(dep):
                    return(False)

            selected.add(crs)
            output.append(crs)
            return(True)
        
        for i in range(numCourses):
            if not _dfs(i):
                return([])


        return(output)