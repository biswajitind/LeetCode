import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjucency List
        adjList = {}
        visited = set()

        for i in range(numCourses):
            adjList[i] = []

        for course, dependency in prerequisites:
                adjList[course].append(dependency)

        def _dfs(course):
            if course in visited:
                return(False)
            if adjList[course] == []:
                return(True)
            
            visited.add(course)
            for dep in adjList[course]:
                if not _dfs(dep):
                    return(False)

            visited.remove(course)
            adjList[course] = []
            return(True)


        # initiate the dfs for each course.
        for i in range(numCourses):
            if not _dfs(i):
                return(False)

        return(True)

