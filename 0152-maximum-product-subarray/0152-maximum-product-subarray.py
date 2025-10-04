class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxProd = max(nums)
        curMax = curMin = 1
        for n in nums:
            tmpMax = curMax * n
            curMax = max(tmpMax, curMin * n, n)
            curMin = min(tmpMax, curMin * n, n)
            maxProd = max(maxProd, curMax)

        return(maxProd)