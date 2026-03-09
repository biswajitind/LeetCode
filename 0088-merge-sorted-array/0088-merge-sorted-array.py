class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = m + n - 1
        m -= 1
        n -= 1
        while n >= 0:
            if m < 0 or nums1[m] <= nums2[n]:
                # simply move the last element from nums2
                nums1[t] = nums2[n]
                t -= 1
                n -= 1
            else:

                # Swap
                nums1[m], nums1[t] = nums1[t], nums1[m]
                t -= 1
                m -= 1
        