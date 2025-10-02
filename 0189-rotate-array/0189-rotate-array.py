class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        def reverse_list(n, s, e):
            while s < e:
                n[s], n[e] = n[e], n[s]
                s += 1
                e -= 1
        
        reverse_list(nums, 0, l - 1)
        reverse_list(nums, 0, k - 1)
        reverse_list(nums, k, l-1 )

        