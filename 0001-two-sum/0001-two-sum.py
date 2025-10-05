class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        cache = {nums[0]: 0}

        for i in range(1, size):
            lookup = target - nums[i]
            if lookup in cache:
                return(i, cache[lookup])
            else:
                cache[nums[i]] = i       