class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        ml, mr = 0, 0 
        for i in range(1, len(height)):
            ml = max(ml, height[i-1])
            maxLeft[i] = ml
        
        for i in range(len(height) - 2, -1, -1):
            print(i)
            mr = max(mr, height[i+1])
            maxRight[i] = mr

        # compute
        result = 0
        for i in range(len(height)):
            result += max(0,   min(maxLeft[i], maxRight[i]) - height[i] )
    
        return(result)

                




            

        
