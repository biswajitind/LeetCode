class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {
            0: 0,
            1: 1,
            2: 2
        }

        def _ways(x: int) -> int:
            if x in cache:
                return(cache[x])

            x_ways = _ways(x-1) + _ways(x-2)
            cache[x] = x_ways
            return(x_ways)
        
        return(_ways(n))

        