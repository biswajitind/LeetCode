class Solution:

    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        ind = -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                ind = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return(ind)


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binSearch(nums, target, True)
        r = self.binSearch(nums, target, False)
        return(l, r)
