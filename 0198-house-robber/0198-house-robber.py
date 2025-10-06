class Solution:        
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def robHouse(i, tnums):
            if i >= len(tnums):
                return(0)
            
            if i in memo:
                return memo[i]
            
            ans = tnums[i] + robHouse(i+2, tnums)
            memo[i] = ans
            return(ans)
        
        return(max(robHouse(0, nums), robHouse(1, nums)))
        