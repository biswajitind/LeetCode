class Solution:
    def climbStairs(self, n: int) -> int:
        prevPrev = 1
        prev = 2

        if n == 0:
            return(0)
        if n <= 2:
            return(n)
        
        for i in range(3, n+1):
            curr = prevPrev + prev
            prevPrev, prev = prev, curr
        return(prev)