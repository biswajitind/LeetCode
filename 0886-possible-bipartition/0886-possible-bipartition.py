class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        folks = {}
        rooms = [0] * (n + 1)
        processed = set()

        # Adjacency list
        for d in dislikes:
            a = d[0]
            b = d[1]
            if a in folks:
                folks[a].append(b)
            else:
                folks[a] = [b]
            if b in folks:
                folks[b].append(a)
            else:
                folks[b] = [a]
        
        def _dfs(x):
            if x in processed:
                return(True)
            else:
                processed.add(x)

            if rooms[x] == 0:
                rooms[x] = -1
            if x in folks:
                for y in folks[x]:
                    if rooms[y] == 0:
                        rooms[y] = rooms[x] * -1
                    else:
                        if rooms[x] == rooms[y]:
                            return(False)
                for y in folks[x]:
                    res = _dfs(y)
                    if res == False:
                        return(False)
                

        for i in range(1, n + 1):
            res = _dfs(i)
            if res == False:
                return(False)
                
        return(True)



        
