class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1. Time O(N^2) Space O(1)
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return([i,j])

        # Solution 2. Time O(N) Space O(N)
        hMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hMap:
                return([hMap[target - nums[i]], i])
            
            hMap[nums[i]] = i