class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        size = len(flowerbed)

        empty = 0
        for i in range(size):
            cur = flowerbed[i]

            if i == size - 1:
                next = 0
            else:
                next =  flowerbed[i+1]

            if cur == 0:
                if prev == 0 and next == 0:
                    n -= 1
                    cur = 1
            
            prev = cur                    
            if n <= 0:
                return(True)
            
        return(False)




