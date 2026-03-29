class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        k1 = k
        for num in nums:
            # if k1 <= 0 :
            #     heapq.heappop(maxHeap)
            #     k1 -= 1

            heapq.heappush(maxHeap, -1 * num)
        
        for i in range(k - 1):
            heapq.heappop(maxHeap)
        
        return(heapq.heappop(maxHeap) * -1)


