class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # With XOR
        # res = 0
        # for n in nums:
        #     res = res ^ n
        # return(res)


        # with hashSet, which will have 
        hs = set()
        for n in nums:
            if n in hs:
                hs.remove(n)
            else:
                hs.add(n)
        return(list(hs)[0])