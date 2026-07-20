class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def _dfs(i, total, cur):
            if total == target:
                result.append(cur.copy())
                return()
            if ((i >= len(candidates)) or (total > target)):
                return()

            

            # cur.append(candidates[i])
            # _dfs(i, total + candidates[i], cur)
            # cur.pop()

            _dfs(i+1, total, cur)

            cur.append(candidates[i])
            _dfs(i, total + candidates[i], cur)
            cur.pop()

        _dfs(0, 0, [])
        return(result)
