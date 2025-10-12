class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {
            0: 0,
            1: 1,
            2: 2
        }

        # def _ways(x: int) -> int:
        #     if x in cache:
        #         return(cache[x])

        #     x_ways = _ways(x-1) + _ways(x-2)
        #     cache[x] = x_ways
        #     return(x_ways)
        
        # return(_ways(n))

        if n in cache:
            return(cache[n])

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
 
        return(cache[n])

        