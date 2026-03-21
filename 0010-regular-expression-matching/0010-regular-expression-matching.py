class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        # Since we will check if the index are outpu bound in multiple places, lets store the 
        # upper indices in the following variables.

        iMax = len(s) - 1
        jMax = len(p) - 1

        depth = 0
        def dfs(i, j, depth):
            depth += 1
            # Memoization
            #print(" " * depth, 'dfs:', i, j)
            if (i, j) in cache:
                return(cache[(i, j)])

            # i, j both out of bound. True    
            if i > iMax and j > jMax:
                cache[(i, j)] = True
                return(True)

            # Only j out of bound. False
            if j > jMax:
                # if j is out of bound, this means i is NOT, which indicates that the pattern
                # has completed but still there are characters in teh string.
                cache[(i, j)] = False
                return(False)

            # current position matches the pattern.
            match = i <= iMax and (s[i] == p[j] or p[j] == '.')

            # current pattern character has a * next to it.
            star = j+1 <= jMax and p[j+1] == '*'

            if match:
                if star:                    
                    cache[(i, j)] = (dfs(i+1, j, depth) or dfs(i, j+2, depth))
                    return(cache[(i, j)])
                else:
                    
                    cache[(i, j)] = (dfs(i+1, j+1, depth))
                    return(cache[(i, j)])
            else:
                if star:
                    
                    cache[(i, j)] = (dfs(i, j+2, depth))
                    return(cache[(i, j)])
                else:
                    cache[(i, j)] = False
                    return(cache[(i, j)])


        return(dfs(0, 0, depth))
                













