class Solution:
    def mySqrt(self, x: int) -> int:

        # binary search iteration starting from 0 till the number.
        l, r = 0, x
        res = 0

        while l <=  r:
            m = l + ((r - l)  // 2 )
            s = m**2
            if s > x:
                r = m - 1
            elif s < x:
                l = m + 1
                res = m
            else:
                return(m)
        return(res)
        