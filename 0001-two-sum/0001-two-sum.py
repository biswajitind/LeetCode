class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return([i, j])
        # return([])
        hMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hMap:
                return([hMap[target - nums[i]], i])
            else:
                hMap[nums[i]] = i

