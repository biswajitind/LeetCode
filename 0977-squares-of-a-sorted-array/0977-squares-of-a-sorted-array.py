class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [None] * len(nums)
        l = 0
        r = len(nums) - 1
        idx = r

        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                result[idx] = nums[r] ** 2
                r -= 1
                idx -= 1
            else:
                result[idx] = nums[l] ** 2
                l += 1
                idx -= 1
        return(result)


            

        