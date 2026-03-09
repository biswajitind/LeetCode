class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        absMin = float("inf")
        for i in range(1, len(arr)):
            curMin = abs(arr[i] - arr[i-1])
            if absMin > curMin:
                absMin = curMin
                result = [[arr[i-1], arr[i]]]
            elif absMin == curMin:
                result.append([arr[i-1], arr[i]])
        return(result)