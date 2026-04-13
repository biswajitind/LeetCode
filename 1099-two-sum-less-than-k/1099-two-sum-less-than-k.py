class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = -1
        l, r = 0, len(nums) - 1
        while l < r:
            twoSum = nums[l] + nums[r]
            if twoSum < k:
                result = max(result, twoSum)
                l += 1
            else:
                r -= 1

        return(result)