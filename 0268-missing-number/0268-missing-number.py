class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tsum = 0
        n = len(nums)
        for num in nums:
            tsum += num
        return(( n * (n+1) // 2 ) - tsum )
        
        