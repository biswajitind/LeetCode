class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # monotonic Stack
        SIZE = len(heights)
        result = [0] * SIZE

        # initialise with known values.
        stack = [heights[-1]]
        result[-1] = 0

        for i in range(SIZE - 2, -1, -1):
            # Nothing in stack.
            count = 0
            if heights[i] > stack[-1]:
                while stack and stack[-1] < heights[i]:
                    stack.pop()
                    count += 1
                
                if stack:
                    count += 1
                result[i] = count
            else:
                result[i] = 1

            stack.append(heights[i])
        
        return(result)
