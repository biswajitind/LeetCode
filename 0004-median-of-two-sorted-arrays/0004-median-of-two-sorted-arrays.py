class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
        total = len(nums1) + len(nums2)
        midFinal = total // 2


        # At this time we have A as the smaller list.
        # this is where we want to perform binary search in order to reduce Time complexity.
        l, r = 0, len(A) - 1
        while True:
            midA = (l + r) // 2
            midB = midFinal - midA - 2

            leftA  = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if midA + 1 < len(A) else float("inf") 
            leftB  = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if midB + 1 < len(B) else float("inf") 

            if leftA <= rightB and leftB <= rightA:
                # if total is a odd number
                if total % 2:
                    return(min(rightA, rightB))
                else:
                    return((max(leftA, leftB) + min(rightA, rightB)) / 2)
            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1



