class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = 1

        for i in range(1, len(nums) + 1):
            if not i in h:
                return(i)
        return(i + 1)
