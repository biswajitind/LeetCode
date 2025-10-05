class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        asum = n * (n+1) // 2
        tsum = 0
        for i in range(n):
            tsum += nums[i]
        return(asum - tsum)
            
        
        