class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        elems = [val for val in range(1, 10)]
        print(elems)
        
        def _dfs(i,total, cur):
            
            count = len(cur)
            print(cur, count, total, k, n)            

            if count == k and total == n:
                result.append(cur.copy())
                return()

            if count > k or total > n or i >= len(elems):
                return()            
            
            cur.append(elems[i])
            _dfs(i+1, total + elems[i], cur)
            cur.pop()

            _dfs(i+1, total , cur)

        _dfs(0,0,[])
        return(result)