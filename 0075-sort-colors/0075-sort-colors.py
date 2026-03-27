class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We will use bucket sort. one iteration to populate the bucket.
        bucket = {}
        for color in nums:
            bucket[color] = bucket.get(color, 0) + 1
        idx = 0
        for i in range(0, 3):
            for j in range(0, bucket.get(i, 0)):
                nums[idx] = i
                idx += 1

        # # One pass, two pointers
        # l, r = 0, len(nums) - 1
        # i = 0 
        # while i <= r:
        #     if nums[i] == 2:
        #         nums[i], nums[r] = nums[r], nums[i]
        #         r -= 1
        #         continue

        #     if nums[i] == 0:
        #         nums[i], nums[l] = nums[l], nums[i]
        #         l += 1
        #     i += 1

