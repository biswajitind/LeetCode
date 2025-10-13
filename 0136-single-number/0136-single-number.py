class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for n in nums:
        #     res = res ^ n
        # return(res)

        # with hashSet
        hs = set()
        for n in nums:
            if n in hs:
                hs.remove(n)
            else:
                hs.add(n)
        return(list(hs)[0])