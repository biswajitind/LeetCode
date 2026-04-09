class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Get the max
        maxIdx = 0
        res = [False] * len(candies)
        for i in range(1, len(candies)):
            if candies[maxIdx] <= candies[i]:
                maxIdx = i

        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= candies[maxIdx]:
                res[i] = True
        return(res)

        


        