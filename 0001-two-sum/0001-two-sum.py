class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute Force
        for i in range(len(nums) -1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return(i, j)
        