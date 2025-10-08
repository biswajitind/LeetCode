class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet = set(nums1)
        result = []

        for n in nums2:
            if n in hashSet:
                result.append(n)
                hashSet.remove(n)
        return(result)
        