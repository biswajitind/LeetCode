class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute Force O(n**2) O(1)
        # for i in range(len(nums) -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return(i, j)
        
        # with HashMap
        cache = {}
        for i in range(len(nums)):
            if target - nums[i] in cache:
                return([cache[target - nums[i]], i])
            else:
                cache[nums[i]] = i