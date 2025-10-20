class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:

        def helper(x):
            if x >= len(nums):
                return(0)
            if x in self.memo:
                return(self.memo[x])
            else:
                res = max(helper(x+2) + nums[x], helper(x+1))
                self.memo[x] = res
            return(res) 

        return(max(helper(0), helper(1)))