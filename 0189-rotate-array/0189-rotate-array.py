class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        def reverse_list(input, start, end):
            while start < end:
                input[start], input[end] = input[end], input[start]
                start += 1
                end -= 1

        k = k % l        
        reverse_list(nums, 0, len(nums) - 1)
        reverse_list(nums, 0, k - 1)
        reverse_list(nums, k, len(nums) - 1)