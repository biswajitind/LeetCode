class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We will use bucket sort. one iteration to populate the bucket.
        bucket = {}
        for color in nums:
            bucket[color] = bucket.get(color, 0) + 1
        print(bucket)
        idx = 0
        for i in range(0, 3):
            for j in range(0, bucket.get(i, 0)):
                nums[idx] = i
                idx += 1
            

        