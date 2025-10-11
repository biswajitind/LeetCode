class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(intervals[i])
        return(merged)