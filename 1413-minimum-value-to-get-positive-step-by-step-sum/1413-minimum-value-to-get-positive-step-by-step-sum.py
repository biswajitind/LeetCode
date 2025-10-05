class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            minSum = (min(minSum, curSum))
        
        return(-minSum + 1 ) if minSum < 1 else 1
