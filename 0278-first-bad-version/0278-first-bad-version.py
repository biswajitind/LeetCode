# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        bad = r = n
        while l <= r:
            m = (r + l) // 2
            if isBadVersion(m):
                r = m - 1
                bad = m
            else:
                l = m + 1
        return(bad)

