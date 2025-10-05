class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # We dont need to compute average for each window, 
        # the sum is enough, we can devide by k and return.

        # first window
        n = len(nums)
        csum = 0
        for i in range(k):
            csum += nums[i]
        maxSum = csum
        # subsequent windows.
        for i in range(k, n):
            csum += nums[i]  
            csum -= nums[i-k]
            maxSum = max(maxSum, csum)
        
        return(maxSum / k)        