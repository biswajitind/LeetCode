class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spaceCount = 1
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i]:
                count += (spaceCount - 1) // 2
                spaceCount = 0
            else:
                spaceCount += 1
            print(i, spaceCount, count, flowerbed[i])

        # remaing spaces till end.
        if spaceCount:
            count += (spaceCount ) // 2

        return(count >= n)