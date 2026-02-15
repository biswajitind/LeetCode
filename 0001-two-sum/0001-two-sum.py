class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hMap:
                return(hMap[target - nums[i]], i)
            else:
                hMap[nums[i]] = i
        
