class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # At max she can eat all the bannanas in a single pile, in single hour
        # ( and min would be 1 at a time)
        # we would check each possibility using binary search to reach the optimum 
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            t = 0
            for i in range(len(piles)):
                t += ceil(piles[i] / mid)
            if t <= h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return(res)
            
        


        