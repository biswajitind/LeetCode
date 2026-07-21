class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def _dfs(i, total, cur):
            if total == target:
                result.append(cur.copy())
                return()
            if total > target or i >= len(candidates):
                return()
            
            # include i. in this increment the pointer by 1 
            cur.append(candidates[i])
            _dfs(i+1, total + candidates[i], cur)
            cur.pop()

            # do not include i, skip all the element same as i 
            skip = 1
            while i + skip < len(candidates) and candidates[i] == candidates[i + skip]:
                skip += 1
            _dfs(i+skip, total, cur)

        _dfs(0,0, [])

        return(result)
        