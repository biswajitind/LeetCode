class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                return(nums[i])
            s[nums[i]] = 1